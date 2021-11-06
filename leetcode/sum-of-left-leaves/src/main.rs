use sum_of_left_leaves::Solution;
use my_utils::*;
fn main() {
    for (inp,out) in [
        (vec![Some(3), Some(9), Some(20), None, None, Some(15), Some(7)], 24),
        (vec![Some(1)], 0),
    ] {
        assert_eq!(Solution::sum_of_left_leaves(create_tree(inp)), out);
    }
}
