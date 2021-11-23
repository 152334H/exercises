pub struct Solution {}
use std::collections::HashMap;
impl Solution {
    pub fn get_primes() -> Vec<i32> {
        let mut primes = vec![2];
        let mut n = 3;
        let ma: i32 = (100000 as f64).sqrt() as i32;
        while n <= ma {
            if primes.iter().all(|&p| n % p != 0) {
                primes.push(n);
            }
            n += 2;
        }
        primes
    }
    pub fn largest_component_size(nums: Vec<i32>) -> i32 {
        let mut ufds = (0..100001).collect::<Vec<_>>();
        fn find(ufds: &mut Vec<i32>, x: i32) -> i32 {
            let xu = x as usize;
            if ufds[xu] != x { ufds[xu] = find(ufds, ufds[xu]) }
            ufds[xu]
        }
        macro_rules! find { ($x:expr) => { find(&mut ufds, $x) }; }
        let mut union = |x: i32, y: i32| {
            let a = find!(y);
            ufds[a as usize] = find!(x);
        };
        
        let primes = Solution::get_primes();
        for &n in nums.iter() {
            let mut rem = n;
            for &p in primes.iter() {
                // try to divide rem by p, and union if possible
                let orem = rem;
                while rem % p == 0 { rem /= p; }
                if orem != rem { union(p, n); }
                // early exit if all divisors have been seen
                if rem == 1 { break; }
            }
            if rem > 1 { union(rem, n); } // rem must be prime here
        }
        let mut cnt = HashMap::new();
        for &n in nums.iter() {
            *cnt.entry(find!(n)).or_insert(0) += 1;
        }
        *cnt.values().max().unwrap() as i32
    }
}
