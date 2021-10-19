use next_greater_element_i::lib::Solution;
fn main() {
    for (n1,n2,o) in [
        (vec![4,1,2], vec![1,3,4,2], vec![-1,3,-1]),
        (vec![2,4],vec![1,2,3,4],vec![3,-1])
    ] {
        assert_eq!(Solution::next_greater_element(n1, n2), o);
    }
}
