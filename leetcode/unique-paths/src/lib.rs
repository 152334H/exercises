pub struct Solution {}
impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        if m == 1 || n == 1 { 1 } else {
            let (mi,ma) = if m > n { (n,m) } else { (m,n) };
            (1..mi as i64).fold(1i64, |acc, i| acc * (ma as i64 + i - 1) / i) as i32
        }
    }
}
