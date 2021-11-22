use my_utils::*;
pub struct Solution {}
type Node = TreeNode;
use std::rc::Rc;
use std::cell::RefCell;
type MaybeNode = Option<Rc<RefCell<Node>>>;
impl Solution {
    pub fn delete_node(root: MaybeNode, v: i32) -> MaybeNode {
        if let Some(ref node) = root {
            let mut node = node.borrow_mut();
            macro_rules! delete_side { ($side:ident) => {
                node.$side = Solution::delete_node(node.$side.clone(), v)
            } }
            if node.val == v { // remove the current node from bst
                return if node.left.is_none() { node.right.clone() }
                else if node.right.is_none() { node.left.clone() }
                else {
                    let mut left = node.left.clone();
                    // move head to the rightmost node
                    // this is some really bad code
                    loop {
                        let tmp = left.clone().unwrap();
                        let mut left_node = tmp.borrow_mut();
                        if let Some(right) = left_node.right.clone() {
                            left.replace(right);
                        } else {
                            left_node.right = node.right.clone();
                            break node.left.clone()
                        }
                    }
                }
            } else if node.val > v { delete_side!(left) }
            else { delete_side!(right) }
        }
        root
    }
}
