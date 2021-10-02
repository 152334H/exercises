use std::io;
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s.trim().to_string();
}
fn main() {
    gets();
    let mut v = [false; 27];
    let s = gets();
    for (i,c) in s.trim().split(' ').enumerate() {
        v[i] = c == "T";
    }
    let s = gets();
    let mut stack: Vec<bool> = Vec::new();
    macro_rules! pop { () => { stack.pop().expect("") }; }
    for c in s.trim().split(' ') {
        let tmp = match c {
            "*" => pop!() & pop!(),
            "+" => pop!() | pop!(),
            "-" => !pop!(),
            _ => v[c.chars().next().unwrap() as usize - 'A' as usize]
        };
        stack.push(tmp);
    }
    println!("{}", if pop!() { "T" } else { "F" });
}
