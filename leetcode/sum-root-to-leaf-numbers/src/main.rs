use sum_root_to_leaf_numbers::Solution;
use my_utils::*;
fn main() {
    for (inp,out) in [
        (vec![1,2,3], 25),
        (vec![4,9,0,5,1], 1026),
    ] {
        assert_eq!(Solution::sum_numbers(create_tree(
            inp.into_iter().map(|v| Some(v)).collect())), out);
    }
}
