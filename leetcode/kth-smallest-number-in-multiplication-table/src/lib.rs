pub struct Solution {}
impl Solution {
    pub fn find_kth_number(m: i32, n: i32, k: i32) -> i32 {
        /* The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).
Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.
        */
        // binary search for the answer
        let mut lo = 0;
        let mut hi = m * n;
        loop {
            if lo >= hi { break lo }
            let mid = lo + (hi-lo)/2;
            let count: i32 = (1..=m).map(|y| (mid/y).min(n)).sum();
            if count < k { lo = mid + 1; }
            else { hi = mid; }
        }
    }
}
