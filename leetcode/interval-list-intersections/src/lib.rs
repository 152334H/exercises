pub struct Solution {}
impl Solution {
    pub fn interval_intersection(first_list: Vec<Vec<i32>>, second_list: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        let (mut i,mut j) = (0,0);
        macro_rules! tupled { ($v:expr) => { ($v[0], $v[1]) } }
        while i < first_list.len() && j < second_list.len() {
            let first = tupled!(first_list[i]);
            let second = tupled!(second_list[j]);
            let start = first.0.max(second.0);
            let end = first.1.min(second.1);
            if start <= end { result.push(vec![start, end]); }
            if first.1 < second.1 { i += 1; }
            else { j += 1; }
        }
        result
    }
}
