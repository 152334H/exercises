use std::collections::{HashMap,VecDeque,BinaryHeap};
use std::convert::TryInto;
use std::cmp::Reverse;
struct Solution<'a> {
    examples: Vec<(Vec<Vec<&'a str>>, Vec<&'a str>)>
}
impl Solution<'_> {
    pub fn find_itinerary(tickets: Vec<Vec<String>>) -> Vec<String> {
        let mut adjls: HashMap<&str,_> = HashMap::new();
        let mut vis = HashMap::new();
        macro_rules! ctr { ($u:expr) => { vis.entry($u).or_insert(0) }; }
        macro_rules! get { ($u:expr) => { adjls.entry($u).or_insert_with(|| BinaryHeap::new()) };}
        for t in &tickets {
            get!(t[0].as_str()).push(Reverse(t[1].as_str()));
            *ctr!(t[1].as_str())+=1;
        }
        //
        let mut q = Vec::new();
        q.push("JFK");
        *ctr!("JFK")+=1;
        let mut euler_path = Vec::new();
        while !q.is_empty() {
            let u = q.last().unwrap();
            match get!(u).pop() {
                Some(v) => q.push(v.0),
                None => euler_path.push(q.pop().unwrap().to_string())
            }
        }
        euler_path.reverse();
        euler_path
    }
    pub fn test(&self) {
        for (input, output) in self.examples.clone() {
            assert_eq!(Solution::find_itinerary(input.iter().map(|t| t.iter().map(|&s| s.to_string()).collect()).collect()), output);
        }
    }
}
fn main() {
    let s = Solution { examples: vec![
        (vec![vec!["JFK","SFO"],vec!["JFK","ATL"],vec!["SFO","ATL"],vec!["ATL","JFK"],vec!["ATL","SFO"]],
        vec!["JFK","ATL","JFK","SFO","ATL","SFO"]),
        (vec![vec!["MUC","LHR"],vec!["JFK","MUC"],vec!["SFO","SJC"],vec!["LHR","SFO"]],
        vec!["JFK","MUC","LHR","SFO","SJC"]),
    ]};
    s.test();
}
