use parallel_courses_iii::lib::Solution;
fn main() {
    for (n,v,t) in [
        (3, vec![vec![1,3],vec![2,3]], vec![3,2,5]),
        (5, vec![vec![1,5],vec![2,5],vec![3,5],vec![3,4],vec![4,5]], vec![1,2,3,4,5])
    ] {
        println!("{}", Solution::minimum_time(n,v,t));
    }
}
