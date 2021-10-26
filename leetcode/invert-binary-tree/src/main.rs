use invert_binary_tree::Solution;
use my_utils::*;
fn main() {
    for (inp,out) in [
        (vec![4,2,7,1,3,6,9], vec![4,7,2,9,6,3,1]),
        (vec![2,1,3], vec![2,3,1]),
    ] {
        let inp: Vec<Option<i32>> = inp.into_iter().map(|v| Some(v)).collect();
        let out: Vec<Option<i32>> = out.into_iter().map(|v| Some(v)).collect();
        assert_eq!(flatten_tree(Solution::invert_tree(create_tree(inp))),flatten_tree(create_tree(out)));

    }
}
