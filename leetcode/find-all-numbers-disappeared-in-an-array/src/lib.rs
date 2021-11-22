pub struct Solution {}
impl Solution {
    pub fn find_disappeared_numbers(mut nums: Vec<i32>) -> Vec<i32> {
        for i in 0..nums.len() {
            let index = (nums[i].abs() as usize) - 1;
            if nums[index] > 0 {
                nums[index] = -nums[index];
            }
        }
        nums.iter().enumerate().filter(|(_,&v)| v>0)
            .map(|(i,_)| i as i32 + 1).collect()
    }
}
