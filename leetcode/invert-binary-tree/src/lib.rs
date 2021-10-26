pub struct Solution {}
use my_utils::*;
use std::rc::Rc;
use std::cell::RefCell;
type MaybeNode = Option<Rc<RefCell<TreeNode>>>;
impl Solution {
    pub fn invert_tree(mut root: MaybeNode) -> MaybeNode {
        Solution::invert_tree_r(&mut root);
        root
    }
    fn invert_tree_r(root: &mut MaybeNode) {
        if let Some(rc) = root {
            let mut n = rc.borrow_mut();
            Solution::invert_tree_r(&mut n.left);
            Solution::invert_tree_r(&mut n.right);
            //std::mem::swap(&mut n.left, &mut n.right);
            let l = n.left.take();
            let r = n.right.take();
            n.left = r; n.right = l;
        }
    }
}
