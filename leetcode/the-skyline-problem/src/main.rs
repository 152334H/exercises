struct Solution {}
use std::convert::TryInto;
use std::collections::BTreeMap;
use std::collections::btree_map::Entry;
impl Solution {
    /* The basic idea is to use an ordered map to represent the skyline.
     * For every building,
         * find the node closest-to && less-than-or-eq-to building.left.
         * while node.x < building.right:
             * update the skyline with the building's height
                 * the hard part here is ensuring duplicate heights don't appear
                 * (i.e. "consecutive horizontal lines of equal height")
             * "increment" the node (like a c++ std::map iterator)
         * update the skyline with the end of the current building
     * Then just walk through the ordered map to get the final skyline.
     */
    pub fn get_skyline(buildings: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut rbtree = BTreeMap::new(); // not actually an rbtree, but similar
        rbtree.insert(0, 0); // pseudo-node to guarantee that equal_or_lower exists.
        macro_rules! equal_or_lower { ($x:expr) => {
            rbtree.range(0..=$x).map(|(&x,&y)| (x,y)).next_back().unwrap()
        } }
        for building in &buildings {
            let [left,right,height]: [i32;3] = building[..].try_into().expect("uh-oh");
            let before_right = equal_or_lower!(right);
            let before_left = equal_or_lower!(left);
            rbtree.insert(left, before_left.1); // create a pseudo-node at rbtree[left]
            // prev_h == "the height of the node before the current one"
            let mut prev_h = if left == 0 { 0 } else { equal_or_lower!(left-1).1 };
            let mut to_rm = Vec::new(); // nodes to delete from the rbtree after the loop
            for (cur_x,cur_h) in rbtree.range_mut(left..right) {
                if *cur_h < height { *cur_h = height; }
                if prev_h == *cur_h { to_rm.push(*cur_x); }
                prev_h = *cur_h;
            } // walk through left..right and update rbtree accordingly
            to_rm.into_iter().map(|x| rbtree.remove(&x)).last();
            // account for height change at building.right
            rbtree.insert(right, before_right.1);
            if prev_h == before_right.1 { rbtree.remove(&right); }
        }
        // get rid of btree[0] if there isn't any actual building there.
        if let Entry::Occupied(zero_e) = rbtree.entry(0) {
            if *zero_e.get() == 0 { zero_e.remove(); }
        }
        rbtree.into_iter().map(|(x,y)| vec![x,y]).collect()
    }
}
fn main() {
    for (i,o) in [
        (vec![vec![2,9,10],vec![3,7,15],vec![5,12,12],vec![15,20,10],vec![19,24,8]], vec![vec![2,10],vec![3,15],vec![7,12],vec![12,0],vec![15,10],vec![20,8],vec![24,0]]),
        (vec![vec![0,2,3],vec![2,5,3]], vec![vec![0,3],vec![5,0]]),
        (vec![vec![0,3,3],vec![1,5,3],vec![2,4,3],vec![3,7,3]], vec![vec![0,3],vec![7,0]]),
        (vec![vec![0,10,2],vec![1,2,5],vec![2,5,1]],vec![vec![0,2],vec![1,5],vec![2,2],vec![10,0]]),
        (vec![vec![4,9,10],vec![4,9,15],vec![4,9,12],vec![10,12,10],vec![10,12,8]], vec![vec![4,15],vec![9,0],vec![10,10],vec![12,0]])
    ] {
        assert_eq!(Solution::get_skyline(i), o);
    }
}
