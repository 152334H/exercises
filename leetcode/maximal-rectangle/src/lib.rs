pub struct Solution {}
impl Solution {
    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
        let mut max = 0;
        if matrix.len() == 0 { return max; }
        let mut heights = vec![0; matrix[0].len()+1];
        let underflow = |i| if i == matrix[0].len() { -1 } else { i as i32 };
        for row in matrix.iter() {
            for i in 0..row.len() {
                heights[i] = if row[i] == '1' { heights[i] + 1 } else { 0 };
            }
            let mut stack = vec![row.len()];
            for i in 0..heights.len() {
                while heights[i] < heights[*stack.last().unwrap()] {
                    let h = heights[stack.pop().unwrap()];
                    let w = i as i32 - underflow(*stack.last().unwrap()) - 1;
                    max = max.max(h * w);
                }
                stack.push(i);
            }
        }
        max
    }
}
