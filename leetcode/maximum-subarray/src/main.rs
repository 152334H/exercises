use maximum_subarray::Solution;
fn main() {
    for (nums,out) in [
        (vec![-2,1,-3,4,-1,2,1,-5,4],6),
        (vec![1],1),
        (vec![5,4,-1,7,8],23)
    ] {
        assert_eq!(Solution::max_sub_array(nums),out);
    }
}
