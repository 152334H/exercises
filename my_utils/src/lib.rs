use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;
type MaybeNode = Option<Rc<RefCell<TreeNode>>>;
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: MaybeNode,
  pub right: MaybeNode,
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
macro_rules! new_node { ($x:expr) => {
    Rc::new(RefCell::new(TreeNode::new($x)))
} }
pub fn create_tree(ls: Vec<Option<i32>>) -> MaybeNode {
    let mut it = ls.into_iter();
    let root = Some(new_node!(it.next().unwrap().unwrap()));
    let mut q = VecDeque::new();
    q.push_back(root.clone());
    while let Some(n) = q.pop_front() {
        if let Some(n) = n {
            let mut r = n.borrow_mut();
            macro_rules! helper { ($child:ident) => {
                if let Some(opt) = it.next() {
                    if let Some(x) = opt {
                        r.$child = Some(new_node!(x));
                        q.push_back(r.$child.clone());
                    };
                } else { break; }
            } }
            helper!(left);
            helper!(right);
        }
    }
    root
}
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
