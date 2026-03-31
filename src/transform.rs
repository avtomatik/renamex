use std::path::Path;

use crate::clean::{clean_string, transliterate};

pub fn transform_filename(file_name: &str) -> String {
    let path = Path::new(file_name);

    let stem = path.file_stem().unwrap().to_string_lossy();
    let ext = path.extension().map(|e| e.to_string_lossy());

    let cleaned = clean_string(&stem);
    let transliterated = transliterate(&cleaned);

    match ext {
        Some(ext) => format!("{}.{}", transliterated, ext),
        None => transliterated,
    }
}
