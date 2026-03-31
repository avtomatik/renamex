use rayon::prelude::*;
use std::fs;
use std::path::{Path, PathBuf};
use tracing::{info, warn};

use crate::error::AppError;
use crate::transform::transform_filename;

pub fn process_files<F>(
    dir: &Path,
    filter: Option<F>,
    verbose: bool,
    dry_run: bool,
) -> Result<(), AppError>
where
    F: Fn(&Path) -> bool + Sync,
{
    use rayon::iter::ParallelBridge;

    let entries = fs::read_dir(dir)?
        .filter_map(Result::ok)
        .map(|e| e.path())
        .filter(|p| p.is_file())
        .par_bridge()
        .filter(|path| filter.as_ref().map(|f| f(path)).unwrap_or(true))
        .map(|path| process_one(&path, dir, verbose, dry_run))
        .collect::<Vec<_>>();

    let mut renamed = 0;
    for res in entries {
        match res {
            Ok(true) => renamed += 1,
            Ok(false) => {}
            Err(e) => warn!("Failed: {}", e),
        }
    }

    info!("Processed {} files", renamed);

    Ok(())
}

fn process_one(path: &Path, dir: &Path, verbose: bool, dry_run: bool) -> Result<bool, AppError> {
    let file_name = match path.file_name().and_then(|n| n.to_str()) {
        Some(name) => name,
        None => return Ok(false), // skip non-UTF8 filenames
    };

    if file_name.starts_with('.') {
        return Ok(false); // skip hidden files
    }

    let new_name = transform_filename(file_name);
    if file_name == new_name {
        return Ok(false);
    }

    let ext = Path::new(file_name)
        .extension()
        .map(|e| e.to_str().unwrap_or_default());
    let new_path = unique_path(dir, &new_name, ext);

    if verbose || dry_run {
        info!(
            "{} -> {}",
            file_name,
            new_path.file_name().unwrap().to_string_lossy()
        );
    }

    if !dry_run {
        fs::rename(path, &new_path)?;
    }

    Ok(true)
}

// Collision-safe unique path
fn unique_path(dir: &Path, base_name: &str, ext: Option<&str>) -> PathBuf {
    let mut candidate = dir.join(base_name);
    let mut counter = 1;

    while candidate.exists() {
        candidate = match ext {
            Some(e) => dir.join(format!("{}_{}.{}", base_name, counter, e)),
            None => dir.join(format!("{}_{}", base_name, counter)),
        };
        counter += 1;
    }

    candidate
}
