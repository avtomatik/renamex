use crate::clean::{clean_string, transliterate};
use std::path::Path;

pub fn transform_filename(file_name: &str) -> String {
    let path = Path::new(file_name);

    let stem = path.file_stem().unwrap_or_default().to_string_lossy();
    let ext = path.extension().map(|e| e.to_string_lossy());

    let cleaned = clean_string(&stem);
    let translit = transliterate(&cleaned);

    match ext {
        Some(ext) => format!("{}.{}", translit, ext),
        None => translit,
    }
}
