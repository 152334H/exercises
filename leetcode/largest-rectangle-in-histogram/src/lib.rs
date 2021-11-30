pub struct Solution {}
impl Solution {
    pub fn largest_rectangle_area(mut heights: Vec<i32>) -> i32 {
        heights.push(0);
        let mut stack = vec![heights.len()-1]; // these are indices into heights[]
        let underflow = |x| if x == heights.len()-1 { -1 } else { x as i32 };
        let mut max = 0;
        for i in 0..heights.len() {
            while heights[i] < heights[*stack.last().unwrap()] {
                let h = heights[stack.pop().unwrap()];
                let w = i as i32 - 1 - underflow(*stack.last().unwrap());
                max = max.max(h * w);
            }
            stack.push(i);
        }
        max
    }
}
