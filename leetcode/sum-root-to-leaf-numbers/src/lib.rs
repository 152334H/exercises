pub struct Solution {}
use my_utils::*;
type MaybeNode = Option<Rc<RefCell<TreeNode>>>;
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn sum_numbers_r(root: &MaybeNode, prefix: i32) -> i32 {
        if let Some(node) = root {
            let node = node.borrow();
            let prefix = prefix * 10 + node.val;
            if node.left.is_none() && node.right.is_none() {
                return prefix;
            }
            Solution::sum_numbers_r(&node.left, prefix) + Solution::sum_numbers_r(&node.right, prefix)
        } else {
            0
        }
    }
     pub fn sum_numbers(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
         Solution::sum_numbers_r(&root, 0)
     }
}
