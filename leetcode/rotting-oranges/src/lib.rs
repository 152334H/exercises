pub struct Solution {}
use std::collections::VecDeque;
impl Solution {
    pub fn oranges_rotting(mut grid: Vec<Vec<i32>>) -> i32 {
        /* for each square on the grid,
         * if the square is 2, floodfill adjacent tiles to be 2, and
         * find the maximum number of minutes that will pass before all oranges are rotten.
         */
        let mut queue: VecDeque<(usize, usize)> = VecDeque::new();
        let mut minutes = 0;
        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                if grid[i][j] == 2 {
                    queue.push_back((i, j));
                }
            }
        }
        if queue.is_empty() { // edited
            minutes += 1; // edited again
        }
        while !queue.is_empty() {
            let size = queue.len();
            for _ in 0..size {
                let (i, j) = queue.pop_front().unwrap();
                if i > 0 && grid[i - 1][j] == 1 {
                    grid[i - 1][j] = 2;
                    queue.push_back((i - 1, j));
                }
                if i < grid.len() - 1 && grid[i + 1][j] == 1 {
                    grid[i + 1][j] = 2;
                    queue.push_back((i + 1, j));
                }
                if j > 0 && grid[i][j - 1] == 1 {
                    grid[i][j - 1] = 2;
                    queue.push_back((i, j - 1));
                }
                if j < grid[0].len() - 1 && grid[i][j + 1] == 1 {
                    grid[i][j + 1] = 2;
                    queue.push_back((i, j + 1));
                }
            }
            minutes += 1;
        }
        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                if grid[i][j] == 1 {
                    return -1;
                }
            }
        }
        minutes-1 // edited
    }
}
