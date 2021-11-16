use largest_divisible_susbet::Solution;
fn main() {
    for (inp,out) in [
        (vec![1,2,3],vec![1,2]),
        (vec![1,2,4,8],vec![1,2,4,8]),
    ] {
        let res = Solution::largest_divisible_subset(inp);
        assert_eq!(res,out);
    }
}
