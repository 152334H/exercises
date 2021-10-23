use find_minimum_in_rotated_sorted_array_ii::lib::Solution;
/* Example 1:
 * Input: nums = [1,3,5]
 * Output: 1
 *
 * Example 2:
 * Input: nums = [2,2,2,0,1]
 * Output: 0
 *
 * Constraints:
 *   n == nums.length
 *   1 <= n <= 5000
 *   -5000 <= nums[i] <= 5000
 *   nums is sorted and rotated between 1 and n times.
 */
fn main() {
    for (inp,out) in [
        (vec![3,4,5,1,2],1),
        (vec![4,5,6,7,0,1,2],0),
        (vec![13,15,17,11],11),
        (vec![11,13,15,17],11),
        (vec![1,3,5],1),
        (vec![2,2,2,0,1],0),
        (vec![2,2,2,2,2],2),
        (vec![1,2,2,2,2],1),
        (vec![1,2,2,2,1],1),
        (vec![2,2,2,2,1],1),
        (vec![3,3,1,3],1),
        (vec![3,3,3,4,3],3),
    ] {
        println!("{:?},{}", inp.as_slice(), out);
        assert_eq!(Solution::find_min(inp), out);
    }
}
