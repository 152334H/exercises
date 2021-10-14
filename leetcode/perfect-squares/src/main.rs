struct Solution {}
impl Solution {
    fn is_square(n:i32) -> bool {
        let root = (n as f64).sqrt().floor() as i32;
        root*root == n
    }
    pub fn num_squares(mut n: i32) -> i32 {
        if Solution::is_square(n) { 1 } else {
            // the result is 4 iff n = (4^k)(8m+7)
            while n&3 == 0 { n >>= 2 } // while n%4==0
            if n&7 == 7 { 4 } else { // if 8m+7 matches
                let new_root = (n as f64).sqrt().floor() as i32;
                for i in 1..=new_root {
                    if Solution::is_square(n-i*i) { return 2; }
                }
                3
            }
        }
    }
}
fn main() {
    assert_eq!(Solution::num_squares(4586), 2);
}
