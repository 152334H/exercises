pub mod lib {
pub struct Solution {}
impl Solution {
    /* In the worst-case situation, this function MUST be O(n).
     * Consider: [k;N-1, k-1] must be solved by a linear search eqiv.
     * But binary search will work fine when there are unique elems.*/
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let mut lo = 0;
        let mut hi = nums.len()-1;
        /* loop invariants:
         * 1. nums[0..lo] is sorted
         * 2. nums[hi..nums.len()] is sorted.
         * 3. (lo..hi).len() > 0
         */
        while lo < hi {
            let mid = lo + (hi-lo)/2;
            if nums[mid] < nums[hi] {
                hi = mid; // (2) holds for mid..nums.len()
            } else if nums[mid] > nums[hi] {
                lo = mid+1; // (1) holds for 0..=mid
            } else { // Screw it, linear search.
                /* At this point, either [mid..=hi] or [0..=mid] contains
                 * a single repeated element. But the only way to figure out
                 * which case is true is to linear search either array.
                 */
                if nums[hi-1] == nums[hi] { // could be [mid..=hi]
                    hi -= 1;
                } else { // [0..=mid] contains the same element. Skip!
                    lo = mid+1;
                }
            }
        }
        nums[lo] // note that lo == hi; either will work.
    }
}
}
