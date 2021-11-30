use largest_rectangle_in_histogram::Solution;
fn main() {
    for (inp,out) in vec![
        (vec![2,1,5,6,2,3],10),
        (vec![2,4],4)
    ] {
        assert_eq!(Solution::largest_rectangle_area(inp),out);
    }
}
