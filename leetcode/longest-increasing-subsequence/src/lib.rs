pub mod lib {
pub struct Solution {}
impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut lis = [0;2501];
        nums.iter().enumerate().map(|(i,&n)| { // for every number,
            for j in 0..i {
                if nums[j] < n && lis[j] > lis[i] {
                    lis[i] = lis[j];
                } // find the LIS before n that can be continued by n
            }
            lis[i] += 1; // account for the addition of n.
            lis[i]
        }).max().unwrap() // get maximum lis.
    }
}
}
