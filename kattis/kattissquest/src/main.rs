use std::io;
use std::process::exit;
use std::collections::BTreeSet;
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s.trim().to_string();
}
fn main() {
    let s = gets();
    let n: usize = s.parse().expect("");
    let mut pool = BTreeSet::new();
    for i in 0..n {
        let s = gets();
        let line: Vec<&str>  = s.split(' ').collect();
        match line[0] {
            "add" => {
                pool.insert((line[1].parse().expect(""),
                             line[2].parse().expect(""), i));
            }, // i is added to allow for duplicate (e,g) pairs.
            "query" => {
                let mut x: usize = line[1].parse().expect("");
                let mut gold: usize = 0;
                while !pool.is_empty() {
                    match pool.range(..(x+1, 0, 0)).rev().next() {
                        Some(&(e,g,i)) => {
                            x -= e;
                            gold += g;
                            pool.remove(&(e,g,i));
                        }, None => { break;}
                    }
                } 
                println!("{}", gold);
            },
            _ => { exit(1); }
        }
    }
}
