use rayon::prelude::*;
use std::path::{Path, PathBuf};
use tracing::{info, warn};
use walkdir::WalkDir;

use crate::error::AppError;
use crate::transform::transform_filename;

pub fn process_files<F>(
    dir: &Path,
    filter: Option<F>,
    recursive: bool,
    verbose: bool,
    dry_run: bool,
) -> Result<(), AppError>
where
    F: Fn(&Path) -> bool + Sync,
{
    use rayon::iter::ParallelBridge;

    let walker = if recursive {
        WalkDir::new(dir).into_iter()
    } else {
        WalkDir::new(dir).max_depth(1).into_iter()
    };

    let results = walker
        .filter_map(Result::ok)
        .map(|e| e.path().to_path_buf())
        .filter(|p| p.is_file())
        .par_bridge()
        .filter(|path| filter.as_ref().map(|f| f(path)).unwrap_or(true))
        .map(|path| process_one(&path, verbose, dry_run))
        .collect::<Vec<_>>();

    let mut renamed = 0;

    for res in results {
        match res {
            Ok(true) => renamed += 1,
            Ok(false) => {}
            Err(e) => warn!("Failed: {}", e),
        }
    }

    info!("Processed {} files", renamed);

    Ok(())
}

fn process_one(path: &Path, verbose: bool, dry_run: bool) -> Result<bool, AppError> {
    let file_name = match path.file_name().and_then(|n| n.to_str()) {
        Some(name) => name,
        None => return Ok(false),
    };

    // skip hidden files
    if file_name.starts_with('.') {
        return Ok(false);
    }

    let new_name = transform_filename(file_name);

    if file_name == new_name {
        return Ok(false);
    }

    let parent = path.parent().unwrap_or_else(|| Path::new("."));
    let new_path = unique_path(parent, &new_name);

    if verbose || dry_run {
        info!(
            "{} -> {}",
            file_name,
            new_path.file_name().unwrap().to_string_lossy()
        );
    }

    if !dry_run {
        std::fs::rename(path, &new_path)?;
    }

    Ok(true)
}

fn unique_path(dir: &Path, file_name: &str) -> PathBuf {
    let mut candidate = dir.join(file_name);
    let mut counter = 1;

    let path = Path::new(file_name);
    let stem = path.file_stem().unwrap_or_default().to_string_lossy();
    let ext = path.extension().map(|e| e.to_string_lossy());

    while candidate.exists() {
        let new_name = match &ext {
            Some(ext) => format!("{}_{}.{}", stem, counter, ext),
            None => format!("{}_{}", stem, counter),
        };

        candidate = dir.join(new_name);
        counter += 1;
    }

    candidate
}
