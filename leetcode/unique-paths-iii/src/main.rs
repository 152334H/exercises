use unique_paths_iii::Solution;
fn main() {
    for (inp,out) in [
        (vec![vec![1,0,0,0],vec![0,0,0,0],vec![0,0,2,-1]], 2),
        (vec![vec![1,0,0,0],vec![0,0,0,0],vec![0,0,0,2]], 4),
        (vec![vec![0,1],vec![2,0]], 0),
    ] {
        assert_eq!(Solution::unique_paths_iii(inp), out);
    }
}
