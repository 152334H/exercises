use multiply_strings::Solution;
fn main() {
    for (n1,n2,out) in [
        ("2","3","6"),
        ("123","456","56088"),
        ("1","1","1"),
        ("0","0","0"),
        ("0","1","0"),
    ] {
        assert_eq!(Solution::multiply(n1.to_string(), n2.to_string()), out.to_string());
    }
}
