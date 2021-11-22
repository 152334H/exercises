use unique_paths::Solution;
fn main() {
    for (m,n,out) in [
        (3,2,3),
        (7,3,28),
        (3,7,28),
        (3,3,6),
        (51, 9, 1916797311)
    ] {
        assert_eq!(Solution::unique_paths(m, n), out);
    }
}
