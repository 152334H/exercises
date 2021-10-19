pub mod lib {
pub struct Solution {}
impl Solution {
    pub fn next_greater_element(subset: Vec<i32>, nums: Vec<i32>) -> Vec<i32> {
        let mut stack = Vec::new();
        let mut nge = [-1;10001];
        for &v in nums.iter().rev() {
            while let Some(top) = stack.pop() {
                if top >= v {
                    stack.push(top);
                    nge[v as usize] = top;
                    break
                }
            }
            stack.push(v);
        }
        subset.into_iter().map(|v| nge[v as usize]).collect()
    }
}
}
