pub mod lib {
use std::collections::HashMap;
use rand::prelude::*;
pub struct RandomizedSet {
    to_ind: HashMap<i32,usize>,
    backing: Vec<i32>
}
impl RandomizedSet {
    pub fn new() -> Self {
        RandomizedSet { to_ind: HashMap::new(), backing: Vec::new() }
    }
    
    pub fn insert(&mut self, val: i32) -> bool {
        if self.to_ind.contains_key(&val) { false } else {
            self.to_ind.insert(val, self.backing.len());
            self.backing.push(val);
            true
        }
    }
    
    pub fn remove(&mut self, val: i32) -> bool {
        if let Some(ind) = self.to_ind.remove(&val) {
            let end = self.backing.pop().unwrap();
            if ind != self.backing.len() {
                self.backing[ind] = end;
                self.to_ind.insert(end, ind);
            }
            true
        } else { false }
    }
    
    pub fn get_random(&self) -> i32 {
        let mut rng = thread_rng();
        self.backing[rng.gen_range(0,self.backing.len())]
    }
}
/*
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */
}
