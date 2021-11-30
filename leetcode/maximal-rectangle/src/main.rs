use maximal_rectangle::Solution;
fn main() {
    for (inp,out) in [
        (vec![vec!['1','0','1','0','0'],
              vec!['1','0','1','1','1'],
              vec!['1','1','1','1','1'],
              vec!['1','0','0','1','0']], 6),
        (vec![], 0),
        (vec![vec!['0']], 0),
        (vec![vec!['1']], 1),
        (vec![vec!['0','0']], 0),
    ] { 
        assert_eq!(Solution::maximal_rectangle(inp), out);
    }
}
