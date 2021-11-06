use single_number_iii::Solution;
fn main() {
    for (inp,out) in vec![
        (vec![1,2,1,3,2,5], vec![3,5]),
        (vec![-1,0], vec![-1,0]),
    ] {
        assert_eq!(Solution::single_number(inp), out);
    }
}
