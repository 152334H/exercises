pub struct CombinationIterator {
    s: Vec<u8>,
    state: Vec<usize>
}

impl CombinationIterator {
    pub fn new(characters: String, combination_length: i32) -> Self {
        CombinationIterator {
            s: characters.into_bytes(),
            state: (0..combination_length as usize).collect()
        }
    }
    fn try_increment(&mut self) -> bool {
        let mut i = self.state.len() - 1;
        while i != usize::MAX {
            if self.state[i] < self.s.len() - self.state.len() + i {
                self.state[i] += 1;
                for j in i + 1..self.state.len() {
                    self.state[j] = self.state[j - 1] + 1;
                }
                return true;
            }
            self.state[i] = usize::MAX; // this should always be replaced
            i -= 1;
        }
        false
    }
    pub fn next(&mut self) -> String {
        let res = self.state.iter().map(|&i| self.s[i] as char).collect();
        self.try_increment();
        res
    }
    pub fn has_next(&self) -> bool {
        self.state[0] < usize::MAX
    }
}

/*
 * Your CombinationIterator object will be instantiated and called as such:
 * let obj = CombinationIterator::new(characters, combinationLength);
 * let ret_1: String = obj.next();
 * let ret_2: bool = obj.has_next();
 */
