use std::io;
use std::collections::{HashMap, HashSet};
use std::convert::TryInto;
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s.trim().to_string();
}
fn to_int(s: &String) -> usize { s.parse().expect("Not an int") }
fn main() {
    //let s = gets(); let n: usize = to_int(&s);
    let n = to_int(&gets());
    for _ in 0..n {
        let m = to_int(&gets());
        let mut adjls = HashMap::new();
        let mut insert = |k,v| adjls.entry(k)
            .or_insert(Vec::new()).push(v);
        for __ in 0..to_int(&gets()) {
            let s = gets();
            let [e,g]: [usize; 2] = s.split(' ')
                .map(|s| to_int(&s.to_string()))
                .collect::<Vec<_>>()[0..2]
                .try_into().expect("could not split");
            insert(e,g);
            insert(g,e);
        }
        let mut seen = HashSet::new();
        let mut bubbles = -1;
        for j in 0..m {
            if seen.contains(&j) { continue; }
            let mut q: Vec<usize> = vec![j];
            while q.len() != 0 {
                let k = q.pop().expect("could not pop");
                if seen.contains(&k) { continue;}
                seen.insert(k);
                match adjls.get(&k) {
                    Some(ls) => {
                        for &e in ls { q.push(e); }
                    }, None => ()
                }
            }
            bubbles+=1;
        }
        println!("{}", bubbles);
    }
}
