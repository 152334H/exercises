pub struct Solution{}
impl Solution {
    pub fn largest_divisible_subset(nums: Vec<i32>) -> Vec<i32> {
        /* Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
         * Si % Sj = 0 or Sj % Si = 0.
         * If there are multiple solutions, return any subset is fine.
         */
        let mut dp = vec![vec![]; nums.len()];
        let mut max_len = 0;
        let mut max_idx = 0;
        for i in 0..nums.len() {
            //dp[i] = vec![nums[i]];
            for j in 0..i {
                if nums[i] % nums[j] == 0 && dp[i].len() < dp[j].len() {
                    dp[i] = dp[j].clone();
                    //dp[i].push(nums[i]);
                }
            }
            dp[i].push(nums[i]);
            if dp[i].len() > max_len {
                max_len = dp[i].len();
                max_idx = i;
            }
        }
        dp[max_idx].sort();
        dp[max_idx].clone()
    }
}
