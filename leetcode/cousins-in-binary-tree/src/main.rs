use cousins_in_binary_tree::Solution;
use my_utils::*;
fn main() {
    let t = create_tree(vec![Some(1), Some(2), Some(3), Some(4)]);
    assert_eq!(false, Solution::is_cousins(t,4,3));
    let t = create_tree(vec![Some(1), Some(2), Some(3), None, Some(4), None, Some(5)]);
    assert_eq!(true, Solution::is_cousins(t,5,4));
    let t = create_tree(vec![Some(1), Some(2), Some(3), None, Some(4)]);
    assert_eq!(false, Solution::is_cousins(t,2,3));
}
