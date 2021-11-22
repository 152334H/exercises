use my_utils::*;
use delete_node_in_a_bst::Solution;
fn main() {
    for (flat,key,out) in [
        (vec![Some(5),Some(3),Some(6),Some(2),Some(4),None,Some(7)], 3, vec![Some(5), Some(2), Some(6), None, Some(4), None, Some(7)]),
        (vec![Some(5),Some(3),Some(6),Some(2),Some(4),None,Some(7)], 0, vec![Some(5),Some(3),Some(6),Some(2),Some(4),None,Some(7)]),
    ] {
        let root = create_tree(flat);
        let res = flatten_tree(Solution::delete_node(root,key));
        let out = flatten_tree(create_tree(out));
        assert_eq!(res, out);
    }

}
