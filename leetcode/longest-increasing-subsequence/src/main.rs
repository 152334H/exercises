/*Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104
*/
use longest_increasing_subsequence::lib::Solution;
fn main() {
    for (nums,out) in [
        (vec![10,9,2,5,3,7,101,18],4),
        (vec![0,1,0,3,2,3],4),
        (vec![7,7,7,7,7,7,7],1)
    ] {
        assert_eq!(Solution::length_of_lis(nums), out);
    }
}
