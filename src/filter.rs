use std::collections::HashSet;
use std::path::Path;

pub fn extension_filter(exts: Vec<String>) -> impl Fn(&Path) -> bool + Sync {
    let exts: HashSet<String> = exts
        .into_iter()
        .map(|e| {
            if e.starts_with('.') {
                e
            } else {
                format!(".{}", e)
            }
        })
        .collect();

    move |path: &Path| {
        path.extension()
            .map(|e| exts.contains(&format!(".{}", e.to_string_lossy())))
            .unwrap_or(false)
    }
}
