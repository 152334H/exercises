pub struct Solution {}

impl Solution {
    pub fn unique_paths_iii(grid: Vec<Vec<i32>>) -> i32 {
        let (mut start, mut end) = ((0,0),(0,0));
        let (max_y, max_x) = (grid.len(), grid[0].len());
        let mut walkable = max_x*max_y;
        for i in 0..max_y {
            for j in 0..max_x {
                match grid[i][j] {
                    1 => start = (i, j),
                    2 => end = (i, j),
                    -1 => walkable -= 1,
                    _ => (),
                }
            }
        }
        // find all hamiltonian paths from start to end
        let mut res = 0;
        let mut q = vec![(start, std::collections::HashSet::<(usize,usize)>::new())];
        while let Some(((i, j), mut visited)) = q.pop() {
            if (i,j) == end {
                res += (visited.len() == walkable-1) as i32;
                continue;
            }
            visited.insert((i,j));
            for &(ny,nx) in &[(i-1,j), (i+1,j), (i,j-1), (i,j+1)] {
                if ny < max_y && nx < max_x && !visited.contains(&(ny,nx)) && grid[ny][nx] != -1 {
                    q.push(((ny, nx), visited.clone()));
                }
            }
        }
        res
    }
}
