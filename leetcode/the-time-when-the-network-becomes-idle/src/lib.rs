pub mod lib {
pub struct Solution {}
impl Solution {
    pub fn network_becomes_idle(edges: Vec<Vec<i32>>, patience: Vec<i32>) -> i32 {
        let n = patience.len();
        let mut g = vec![Vec::new();n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut d = 0;
        let mut q = vec![0];
        let mut seen = vec![false;n];
        let mut dist = vec![1<<30;n];
        while !q.is_empty() {
            let mut new_q = vec![];
            for u in q {
                if !seen[u] {
                    seen[u] = true;
                    dist[u] = d;
                    new_q.extend(g[u].iter());
                }
            }
            q = new_q;
            d += 1;
        }
        (1..n).map(|i| {
            let d = 2*dist[i];
            d+((d as f64 / patience[i] as f64).ceil() as usize-1)*patience[i] as usize
        }).max().unwrap() as i32 + 1
    }
}
}
