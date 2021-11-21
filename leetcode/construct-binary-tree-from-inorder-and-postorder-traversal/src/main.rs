use my_utils::*;
use construct_binary_tree_from_inorder_and_postorder_traversal::*;
fn main() {
    for (inorder, postorder, out) in [
        (vec![9,3,15,20,7], vec![9,15,7,20,3], vec![Some(3),Some(9),Some(20),None,None,Some(15),Some(7)]),
        (vec![-1],vec![-1],vec![Some(-1)]),
    ] {
        let res = Solution::build_tree(inorder, postorder);
        assert_eq!(flatten_tree(res), flatten_tree(create_tree(out)));
    }
}
