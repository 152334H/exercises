pub struct Solution {}
use my_utils::*;
type MaybeNode = Option<Rc<RefCell<TreeNode>>>;
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn sum_left_r(root: &MaybeNode, left: bool) -> i32 {
        if let Some(node) = root {
            let node = node.borrow();
            if node.left.is_none() && node.right.is_none() {
                left as i32 * node.val
            } else {
                Solution::sum_left_r(&node.left, true) +
                Solution::sum_left_r(&node.right, false)
            }
        } else { 0 }
    }
    pub fn sum_of_left_leaves(root: MaybeNode) -> i32 {
        Solution::sum_left_r(&root, false)
    }
}
