use std::io;
use std::cmp::Ordering;
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s.trim().to_string();
}
fn main() {
    let s = gets();
    let mut prev = gets();
    let mut gt = false;
    let mut lt = false;
    for _i in 1..s.parse().expect("") {
        let cur = gets();
        match cur.cmp(&prev) {
            Ordering::Greater => { gt = true },
            Ordering::Less => { lt = true },
            Ordering::Equal => { lt = true; gt = true}
        };
        if gt && lt {
            println!("NEITHER");
            return;
        }
        prev = cur;
    }
    if gt {
        println!("INCREASING");
    } else {
        println!("DECREASING");
    }
}
