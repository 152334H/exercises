use interval_list_intersections::*;
fn main() {
    for (first,second,out) in [
        (vec![vec![0,2],vec![5,10],vec![13,23],vec![24,25]], vec![vec![1,5],vec![8,12],vec![15,24],vec![25,26]], vec![vec![1,2],vec![5,5],vec![8,10],vec![15,23],vec![24,24],vec![25,25]]),
        (vec![vec![1,3],vec![5,9]], vec![], vec![]),
        (vec![],vec![vec![4,8],vec![10,12]], vec![]),
        (vec![vec![1,7]],vec![vec![3,10]],vec![vec![3,7]]),
    ] {
        assert_eq!(Solution::interval_intersection(first,second),out);
    }
}
