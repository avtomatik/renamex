use std::fs;
use std::path::Path;

use crate::transform::transform_filename;

pub fn process_files(
    dir: &Path,
    filter: Option<&impl Fn(&Path) -> bool>,
    verbose: bool,
) -> Result<(), Box<dyn std::error::Error>> {
    let entries = fs::read_dir(dir)?;

    let mut count = 0;

    for entry in entries {
        let path = entry?.path();

        if !path.is_file() {
            continue;
        }

        if let Some(f) = filter {
            if !f(&path) {
                continue;
            }
        }

        let file_name = path.file_name().unwrap().to_string_lossy();
        let new_name = transform_filename(&file_name);

        if file_name == new_name {
            continue;
        }


        let new_path = dir.join(&new_name);
        fs::rename(&path, &new_path)?;

        if verbose {
            println!("{} -> {}", file_name, new_name);
        }

        count += 1;
    }

    if count == 0 {
        println!("No files renamed");
    } else {
        println!("Processed {} files", count);
    }

    Ok(())
}
