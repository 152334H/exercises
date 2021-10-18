// Definition for a binary tree node.
use my_utils::*;
pub struct Solution {}
use std::rc::Rc;
use std::cell::RefCell;
type MaybeNode = Option<Rc<RefCell<TreeNode>>>;
impl Solution {
    fn depth_and_parent_of(root: &MaybeNode, n: i32) -> Option<(i32,Option<i32>)> {
        if let Some(rc) = root {
            let r = rc.borrow();
            macro_rules! helper { ($child:expr,$end:expr) => {
                if let Some((depth,parent)) = Solution::depth_and_parent_of($child,n) {
                    if let Some(p_val) = parent {
                        Some((depth+1,Some(p_val)))
                    } else { Some((depth+1, Some(r.val))) } 
                } else { $end }
            } }
            if r.val == n { Some((0,None)) } else {
                helper!(&r.left, helper!(&r.right, None))
            }
        } else { None }

    }
    pub fn is_cousins(root: MaybeNode, x: i32, y: i32) -> bool {
        let (depth_x, parent_x) = Solution::depth_and_parent_of(&root,x).unwrap();
        let (depth_y, parent_y) = Solution::depth_and_parent_of(&root,y).unwrap();
        parent_x != parent_y && depth_x == depth_y
    }
}
