use std::io;
use std::collections::{HashMap,BinaryHeap,HashSet};
use std::cmp::Reverse;
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
    // read input
    let m = gets().split(' ').map(to_int).last().unwrap();
    let mut g = HashMap::<usize,HashMap<_,_>>::new();
    macro_rules! get {
        ($k:expr) => { g.entry($k).or_default() }
    }
    for _ in 0..m {
        let tmp = get_vec_of_ints();
        let (a,b,d) = (tmp[0],tmp[1],tmp[2]);
        get!(a).insert(b,d);
        get!(b).insert(a,d);
    }
    // do a reverse dijkstra from the end node
    let mut shortest = HashMap::new();
    let mut pq: BinaryHeap<Reverse<(usize,usize,usize)>> = g.entry(1)
        .or_insert_with(HashMap::new).iter()
        .map(|(&k,&v)| Reverse((v,k,1))).collect();
    while let Some(Reverse((total_dist, node, prev))) = pq.pop() {
        if shortest.contains_key(&node) { continue; }
        shortest.insert(node, prev);
        for (oth,w) in get!(node).iter() {
            pq.push(Reverse((total_dist+w, *oth, node)));
        }
    }
    // prune edges that involve the fastest possible paths
    for (node,nxt) in shortest.iter() {
        g.get_mut(node).unwrap().remove(nxt);
    }
    // attempt dfs from node 0 to 1
    fn trav(vis: &mut HashSet<usize>,
            g: &HashMap<usize,HashMap<usize,usize>>,
            n: usize) -> Option<Vec<usize>> {
        if n == 1 { Some(vec![1]) }
        else if vis.contains(&n) { None }
        else {
            vis.insert(n);
            if let Some(others) = g.get(&n) {
                for &nxt in others.keys() {
                    if let Some(mut path) = trav(vis, g, nxt) {
                        path.push(n);
                        return Some(path);
                    }
                }
            }
            None
        }
    } // will return a path from 1 to 0, if it exists.
    println!("{}", trav(&mut HashSet::new(), &g, 0).and_then(|his|
        Some(format!("{} {}", his.len(), his.into_iter().rev().map(
            |v| v.to_string()).fold(String::new(), |a,s| a+" "+&s))))
        .unwrap_or("impossible".to_string()));
}
