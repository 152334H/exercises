use rotting_oranges::Solution;
fn main() {
    for (inp,out) in [
        (vec![vec![2,1,1],vec![1,1,0],vec![0,1,1]], 4),
        (vec![vec![2,1,1],vec![0,1,1],vec![1,0,1]], -1),
        (vec![vec![0,2]], 0)
    ] {
        assert_eq!(Solution::oranges_rotting(inp), out);
    }
}
