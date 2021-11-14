use daily_temperatures::Solution;
fn main() {
    for (inp,out) in [
        (vec![73, 74, 75, 71, 69, 72, 76, 73], vec![1, 1, 4, 2, 1, 1, 0, 0]),
        (vec![30,40,50,60], vec![1,1,1,0]),
        (vec![30,60,90], vec![1,1,0]),
    ] {
        assert_eq!(Solution::daily_temperatures(inp), out);
    }
}
