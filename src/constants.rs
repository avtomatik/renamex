use std::collections::HashMap;
use once_cell::sync::Lazy;

pub static CYRILLIC_MAP: Lazy<HashMap<char, &'static str>> = Lazy::new(|| {
    let mut m = HashMap::new();

    let letters = vec![
        "a","b","v","g","d","e","zh","z","i","y","k","l","m","n",
        "o","p","r","s","t","u","f","kh","ts","ch","sh","shch",
        "","y","","e","yu","ya","yo"
    ];

    for (i, val) in letters.iter().enumerate() {
        let ch = char::from_u32(1072 + i as u32).unwrap();
        m.insert(ch, *val);
    }

    m.insert('ё', "yo");
    m
});
