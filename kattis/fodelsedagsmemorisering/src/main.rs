use std::io;
use std::collections::HashMap;
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s.trim().to_string();
}
fn to_int(s: &str) -> usize { s.parse().expect("to_int failure") }
fn main() {
    let n = to_int(&gets());
    let mut memory = HashMap::new();
    for _ in 0..n {
        let line = gets();
        let mut fields = line.split(' ');
        let name = fields.next().unwrap();
        let value = to_int(fields.next().unwrap());
        let bday = fields.next().unwrap();
        let entry = memory.entry(bday.to_owned()).or_insert((value,name.to_owned()));
        if entry.0 < value {
            *entry = (value,name.to_owned());
        }
    }
    println!("{}", memory.len());
    let mut lex: Vec<String> = memory.drain().map(|(_,(_,s))| s).collect();
    lex.sort();
    for s in lex { println!("{}", s); }
}
