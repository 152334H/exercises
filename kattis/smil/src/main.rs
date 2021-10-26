use std::io;
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s.trim().to_string();
}
const EYES: [u8;2] = [':' as u8, ';' as u8];
fn main() {
    let tmp = gets();
    let s = tmp.as_bytes();
    for (i,&c) in s[..].iter().enumerate() {
        if i == 0 { continue }
        if c == ')' as u8 {
            if EYES.contains(&s[i-1]) { println!("{}", i-1) }
            else if i > 1 && s[i-1] == '-' as u8 && EYES.contains(&s[i-2]) {
                println!("{}", i-2);
            }
        }
    }
}
