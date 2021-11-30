pub struct Solution {}

impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut max_sum = nums[0];
        let mut cur_sum = nums[0];
        for i in 1..nums.len() {
            cur_sum = std::cmp::max(nums[i], cur_sum + nums[i]);
            max_sum = std::cmp::max(max_sum, cur_sum);
        }
        max_sum
    }
}
