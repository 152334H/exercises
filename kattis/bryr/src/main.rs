use std::io;
use std::cmp::Reverse;
use std::collections::{HashMap,BinaryHeap,HashSet};
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s.trim().to_string();
}
fn to_int(s: &str) -> usize { s.parse().expect("to_int failure") }
fn get_vec_of_ints() -> Vec<usize> {
    gets().split(' ').map(to_int).collect()
}

fn main() {
    let tmp = get_vec_of_ints();
    let (n,m) = (tmp[0], tmp[1]);
    let mut graph = HashMap::new();
    macro_rules! get { ($v:expr) => {
        graph.entry($v).or_insert_with(|| HashMap::new())
    } }
    for _ in 0..m {
        let tmp = get_vec_of_ints();
        let (a,b,c) = (tmp[0],tmp[1],tmp[2]);
        get!(a).insert(b,c);
        get!(b).insert(a,c);
    }
    let mut pq = BinaryHeap::new();
    let mut seen = HashSet::new();
    pq.push(Reverse((0,1)));
    while !pq.is_empty() {
        let Reverse((dist,node)) = pq.pop().unwrap();
        if seen.contains(&node) { continue; }
        if node == n { println!("{}", dist); break; }
        for (oth,d) in get!(node) {
            pq.push(Reverse((dist+*d,*oth)));
        }
        seen.insert(node);
    }
}
