use path_sum_iii::lib::*;
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;
macro_rules! new_node { ($x:expr) => {
    Rc::new(RefCell::new(TreeNode::new($x)))
} }
fn create_tree(ls: Vec<Option<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
    let mut it = ls.into_iter();
    let root = Some(new_node!(it.next().unwrap().unwrap()));
    let mut q = VecDeque::new();
    q.push_back(root.clone());
    while let Some(n) = q.pop_front() {
        if let Some(n) = n {
            let mut r = n.borrow_mut();
            //
            if let Some(opt) = it.next() {
                if let Some(x) = opt {
                    r.left = Some(new_node!(x));
                    q.push_back(r.left.clone());
                };
            } else { break; }
            //
            if let Some(opt) = it.next() {
                if let Some(x) = opt {
                    r.right = Some(new_node!(x));
                    q.push_back(r.right.clone());
                };
            } else { break; }
        }
    }
    root
}
pub fn trav(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Option<i32>> {
	let mut v = Vec::new();
	let mut q = VecDeque::new();
	q.push_back(root);
	while let Some(n) = q.pop_front() { 
		v.push(if let Some(n) = n {
			let r = n.borrow();
			q.push_back(r.left.clone());
			q.push_back(r.right.clone());
			Some(r.val)
		} else { None });
	}
	v
}
fn main() {
    let t = create_tree(vec![Some(10),Some(5),Some(-3),Some(3),Some(2),None,Some(11),Some(3),Some(-2),None,Some(1)]);
    assert_eq!(3, Solution::path_sum(t,8));
    let t = create_tree(vec![Some(5),Some(4),Some(8),Some(11),None,Some(13),Some(4),Some(7),Some(2),None,None,Some(5),Some(1)]);
    assert_eq!(3, Solution::path_sum(t,22));
}
