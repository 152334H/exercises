pub mod lib {
// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}
pub struct Solution{}
use std::rc::Rc;
use std::cell::RefCell;
type MaybeNode = Option<Rc<RefCell<TreeNode>>>;
impl Solution {
    fn recur(parent: &MaybeNode, target_sum: i32) -> (Vec<i64>,usize) {
        let mut possible = Vec::new();
        let mut output = 0;
        if let Some(rc) = parent {
            let r = rc.borrow();
            possible.push(r.val as i64);
            //
            for side in &[&r.left, &r.right] { 
                let (kids,sums) = Solution::recur(side, target_sum);
                for v in kids { possible.push(v+r.val as i64); }
                output += sums;
            }
        }
        output += possible.iter().filter(|&&v| v == target_sum as i64).count();
        (possible,output)
    }
    pub fn path_sum(root: MaybeNode, target_sum: i32) -> i32 {
        Solution::recur(&root, target_sum).1 as i32
    }
}
}
