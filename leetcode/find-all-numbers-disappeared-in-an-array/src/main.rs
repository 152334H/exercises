use find_all_numbers_disappeared_in_an_array::Solution;
fn main() {
    for (inp,out) in [
        (vec![4,3,2,7,8,2,3,1],vec![5,6]),
        (vec![1,1],vec![2]),
    ] {
        assert_eq!(Solution::find_disappeared_numbers(inp),out);
    }
}
