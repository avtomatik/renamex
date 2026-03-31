use regex::Regex;
use crate::constants::CYRILLIC_MAP;

pub fn clean_string(input: &str) -> String {
    let re = Regex::new(r"[^\w]+").unwrap();

    re.split(input.trim())
        .filter(|s| !s.is_empty())
        .collect::<Vec<_>>()
        .join("_")
}

pub fn transliterate(input: &str) -> String {
    input
        .to_lowercase()
        .chars()
        .map(|c| CYRILLIC_MAP.get(&c).unwrap_or(&c.to_string().as_str()).to_string())
        .collect()
}
