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
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;
struct Solution {
}
impl Solution {
    pub fn bst_from_preorder_r<'a>(preorder: &mut std::iter::Peekable<std::slice::Iter<'a, i32>>, rng: std::ops::Range<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut root = TreeNode::new(*preorder.next().unwrap());
        if let Some(&nxt) = preorder.peek() {
            if rng.contains(nxt) && *nxt < root.val {
                root.left = Solution::bst_from_preorder_r(preorder, rng.start..root.val);
            }
        }
        if let Some(&nxt) = preorder.peek() {
            if rng.contains(nxt) && *nxt > root.val {
                root.right = Solution::bst_from_preorder_r(preorder, root.val..rng.end);
            }
        }
        Some(Rc::new(RefCell::new(root)))
    }
    pub fn bst_from_preorder(preorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut it = preorder.iter().peekable();
        Solution::bst_from_preorder_r(&mut it, 0..1001)
    }
    pub fn trav(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut v = Vec::new();
        let mut q = VecDeque::new();
        q.push_back(root);
        while let Some(n) = q.pop_front() { 
            v.push(if let Some(n) = n {
                let r = n.borrow();
                q.push_back(r.left.clone());
                q.push_back(r.right.clone());
                r.val
            } else { 0 });
        }
        v
    }
}
fn main() {
    for (input,output) in [
        (vec![8,5,1,7,10,12], vec![8,5,10,1,7,0,12])
    ] {
        assert_eq!(Solution::trav(Solution::bst_from_preorder(input)), output);
    }
}
