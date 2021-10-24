pub mod lib {
pub struct Solution{}
use std::collections::{HashSet,HashMap,BinaryHeap};
use std::cmp::Reverse;
impl Solution {
    pub fn minimum_time(n: i32, relations: Vec<Vec<i32>>, time: Vec<i32>) -> i32 {
        let mut not_starts = HashSet::new();
        let mut requires = HashMap::new();
        let mut graph = HashMap::new();
        for vec in relations {
            let (p,n) = (vec[0], vec[1]);
            graph.entry(p).or_insert_with(HashSet::new).insert(n);
            not_starts.insert(n);
            requires.entry(n).or_insert_with(HashSet::new).insert(p);
        }

        let mut pq: BinaryHeap<(Reverse<i32>,i32)> = (1..=n)
            .filter(|i| !not_starts.contains(i))
            .map(|i| (Reverse(time[i as usize-1]),i))
            .collect();
        let mut last = 0;
        while let Some((end_time,node)) = pq.pop() {
            let end_time = end_time.0;
            for nxt in graph.entry(node).or_insert_with(HashSet::new).iter() {
                requires.entry(*nxt).or_insert_with(HashSet::new).remove(&node);
                if requires[nxt].is_empty() {
                    pq.push((Reverse(time[*nxt as usize-1]+end_time), *nxt));
                }
            }
            last = end_time
        }
        last
    }
}
}
