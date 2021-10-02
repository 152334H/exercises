use std::io;
use std::collections::HashSet;
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s.trim().to_string();
}
fn to_int(s: &str) -> usize { s.parse().expect("to_int failure") }
fn main() {
    let n = to_int(&gets());
    let mut proofs = HashSet::new();
    for i in 1..=n {
        let line = gets();
        let mut parts = line.split("-> "); // note: not " -> ".
        let assumptions: Vec<&str> = parts.next().unwrap().split(' ').collect();
        let conclusion = parts.next().unwrap();
        for a in assumptions {
            // there will always be one empty element in the assumptions
            if !a.is_empty() && !proofs.contains(a) {
                println!("{}", i);
                return;
            }
        }
        proofs.insert(conclusion.to_owned());
    }
    println!("correct");
}
