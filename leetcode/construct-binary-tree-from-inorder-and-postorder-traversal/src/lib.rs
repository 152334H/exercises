use my_utils::*;
pub struct Solution {}
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashMap;
type MaybeNode = Option<Rc<RefCell<TreeNode>>>;
impl Solution {
    pub fn build_tree(inorder: Vec<i32>, postorder: Vec<i32>) -> MaybeNode {
        let inorder_map: HashMap<i32,usize> = inorder
            .iter().enumerate().map(|(i,&x)| (x,i)).collect();
        Solution::build_tree_r(&inorder_map, &mut postorder.into_iter().rev(), &inorder, 0)
    }
    pub fn build_tree_r(inorder_map: &HashMap<i32,usize>,
            postorder: &mut impl std::iter::Iterator<Item=i32>,
            inorder: &[i32], in_i: usize)
        -> MaybeNode {
        macro_rules! recurse {
            ($inorder: expr, $ind: expr) => { Solution::
                build_tree_r(inorder_map, postorder, $inorder, $ind)
            }
        }
        if inorder.is_empty() { None } else {
            let root_val = postorder.next().unwrap();
            let mut root = TreeNode::new(root_val);
            let right_i = inorder_map[&root_val]+1;
            root.right = recurse!(&inorder[right_i-in_i..], right_i);
            root.left = recurse!(&inorder[..inorder_map[&root_val]-in_i], in_i);
            Some(Rc::new(RefCell::new(root)))
        }
    }
}
