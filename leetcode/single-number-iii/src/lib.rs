pub struct Solution {}
impl Solution {
    pub fn single_number(nums: Vec<i32>) -> Vec<i32> {
        // first, find the xor of the two unique numbers
        let xor = nums.iter().fold(0, |acc, &x| acc ^ x);
        // then, use that information to find the unique numbers
        let mask = xor & !(xor - 1); // first set bit
        let mut res = vec![0,0];
        for x in nums { res[(x & mask == 0) as usize] ^= x; }
        res
    }
}
