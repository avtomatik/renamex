use once_cell::sync::Lazy;
use regex::Regex;

use crate::constants::CYRILLIC_MAP;

static CLEAN_RE: Lazy<Regex> = Lazy::new(|| Regex::new(r"[^\w]+").unwrap());

pub fn clean_string(input: &str) -> String {
    CLEAN_RE
        .split(input.trim())
        .filter(|s| !s.is_empty())
        .collect::<Vec<_>>()
        .join("_")
}

pub fn transliterate(input: &str) -> String {
    input
        .to_lowercase()
        .chars()
        .map(|c| {
            CYRILLIC_MAP
                .get(&c)
                .unwrap_or(&c.to_string().as_str())
                .to_string()
        })
        .collect()
}
