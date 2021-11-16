use kth_smallest_number_in_multiplication_table::Solution;
fn main() {
    for (m,n,k,out) in [
        (3,3,5,3),
        (2,3,6,6),
        (9895, 28405, 100787757,0) // not sure what the right answer is for this one
    ] {
        assert_eq!(Solution::find_kth_number(m, n, k), out);
    }
}
