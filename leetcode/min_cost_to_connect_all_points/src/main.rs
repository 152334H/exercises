use std::collections::HashMap;
struct Solution<'a> {
    output: i32,
    input: &'a [[i32;2]],
}
impl Solution<'_> {
    /* this is NOT the most efficient solution to the problem!
     * "Line sweep algorithm" can be used for O(NlogN) speed
     * instead of O((E+N)logN) speed as with Krustal's.
     */
    pub fn min_cost_connect_points(points: Vec<Vec<i32>>) -> i32 {
        // some helper functions
        fn mhat_dist(a: &[i32], b: &[i32]) -> i32 {
            a.iter().enumerate().map(|(i,&v)| (b[i]-v).abs()).sum()
        }
        // get edges
        let nodes: Vec<&[i32]> = points.iter().map(|a| a.as_slice()).collect();
        let mut edges = Vec::new();
        for i in 0..(nodes.len()-1) {
            for j in 1..nodes.len() {
                let (a,b) = (nodes[i], nodes[j]);
                edges.push((mhat_dist(a,b), a, b));
            }
        }
        edges.sort();
        // run Krustal's algo. I think.
        let mut parent: HashMap<&[i32],&[i32]> = HashMap::new();
        fn findset<'a>(parent: &mut HashMap<&'a[i32],&'a [i32]>, a: &'a[i32]) -> &'a[i32] {
            if *parent.entry(a).or_insert(a) == a  { a } else {
                *parent.entry(a).or_insert(a) = findset(parent,parent[a]);
                parent[a]
            }
        }
        macro_rules! findset { ($a:expr) => { findset(&mut parent, $a); } }
        let mut total = 0;
        for (d,a,b) in edges {
            let (x,y) = (findset!(a), findset!(b));
            if x != y {
                total += d;
                *parent.entry(x).or_insert(x) = y;
            }
        }
        total
    }
    fn test(&self) {
        assert_eq!(self.output, Solution::min_cost_connect_points(self.input.iter().map(|&a| a.into()).collect()));
    }
}

fn main() {
    let s1 = Solution {
        output: 20,
        input: &[[0,0],[2,2],[3,10],[5,2],[7,0]],
    };
    s1.test();
}
