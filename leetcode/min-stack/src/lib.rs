use std::collections::BTreeMap;
pub struct MinStack {
    sorted: BTreeMap<i32,usize>,
    stack: Vec<i32>
}
impl MinStack {
    pub fn new() -> Self {
        MinStack { sorted: BTreeMap::new(), stack: Vec::new() }
    }
    pub fn push(&mut self, val: i32) {
        *self.sorted.entry(val).or_insert(0) += 1;
        self.stack.push(val);
    }
    pub fn pop(&mut self) {
        let k = self.stack.pop().unwrap();
        let v = self.sorted.get_mut(&k).unwrap();
        if *v > 1 { *v -= 1; } else {
            self.sorted.remove(&k);
        }
    }
    pub fn top(&self) -> i32 {
        *self.stack.last().unwrap()
    }
    pub fn get_min(&self) -> i32 {
        *self.sorted.iter().next().unwrap().0
    }
}
