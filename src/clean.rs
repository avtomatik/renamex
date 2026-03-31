use crate::constants::CYRILLIC_MAP;
use once_cell::sync::Lazy;
use regex::Regex;

static CLEAN_RE: Lazy<Regex> = Lazy::new(|| Regex::new(r"[^\w]+").unwrap());

pub fn clean_string(input: &str) -> String {
    CLEAN_RE.replace_all(input.trim(), "_").to_string()
}

pub fn transliterate(input: &str) -> String {
    let mut out = String::with_capacity(input.len());
    for c in input.to_lowercase().chars() {
        if let Some(repl) = CYRILLIC_MAP.get(&c) {
            out.push_str(repl);
        } else {
            out.push(c);
        }
    }
    out
}
