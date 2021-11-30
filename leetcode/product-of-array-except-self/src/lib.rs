pub struct Solution {}
impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let res = vec![1; nums.len()];
        // e.g. nums = [1,2,3,4,5]
        for i in 1..nums.len() {
            res[i] = res[i - 1] * nums[i - 1];
        }
        // then res = [1,1,2,6,24]
        let mut right = 1;
        for i in (0..nums.len()).rev() {
            res[i] *= right;
            right *= nums[i];
        }
        // finally res = [120,60,40,30,24]
        res
    }
}
