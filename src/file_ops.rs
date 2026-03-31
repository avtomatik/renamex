use rayon::prelude::*;
use std::fs;
use std::path::{Path, PathBuf};
use tracing::{info, warn};

use crate::error::AppError;
use crate::transform::transform_filename;

pub fn process_files(
    dir: &Path,
    filter: Option<&(impl Fn(&Path) -> bool + Sync)>,
    verbose: bool,
    dry_run: bool,
) -> Result<(), AppError> {
    let entries: Vec<PathBuf> = fs::read_dir(dir)?
        .filter_map(|e| e.ok().map(|e| e.path()))
        .filter(|p| p.is_file())
        .collect();

    let results: Vec<_> = entries
        .par_iter()
        .filter(|path| if let Some(f) = filter { f(path) } else { true })
        .map(|path| process_one(path, dir, verbose, dry_run))
        .collect();

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

fn process_one(path: &Path, dir: &Path, verbose: bool, dry_run: bool) -> Result<bool, AppError> {
    let file_name = path.file_name().unwrap().to_string_lossy();
    let new_name = transform_filename(&file_name);

    if file_name == new_name {
        return Ok(false);
    }

    let new_path = dir.join(&new_name);

    // prevent overwrite
    if new_path.exists() {
        warn!("Skipping (exists): {}", new_name);
        return Ok(false);
    }

    if verbose || dry_run {
        info!("{} -> {}", file_name, new_name);
    }

    if !dry_run {
        fs::rename(path, new_path)?;
    }

    Ok(true)
}
