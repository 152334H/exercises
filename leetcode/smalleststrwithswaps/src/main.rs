use std::collections::{HashSet,HashMap};
pub fn smallest_string_with_swaps(s: String, pairs: Vec<Vec<i32>>) -> String {
    let mut adjls = HashMap::new();
    macro_rules! getentry {
        ($u:expr) => {
            adjls.entry($u).or_insert_with(Vec::new);
        };
    }
    for e in pairs {
        getentry!(e[0]).push(e[1]);
        getentry!(e[1]).push(e[0]);
    }
    let mut seen = HashSet::new();
    let mut sets = Vec::new();
    for i in 0..(s.len() as i32) {
        if !adjls.contains_key(&i) || seen.contains(&i) {
            continue;
        }
        let mut q = vec![i];
        let mut g = HashSet::new();
        while !q.is_empty() {
            let nxt = q.pop().expect("pop failure");
            if seen.contains(&nxt) { continue; }
            seen.insert(nxt);
            for v in getentry!(nxt) { q.push(*v); }
            g.insert(nxt);
        }
        sets.push(g);
    }
    let mut t = vec![b'\0'; s.len()];
    let b = s.into_bytes();
    for g in sets {
        let mut chars = g.iter().map(|&i| b[i as usize]).collect::<Vec<u8>>();
        let mut sorted_g: Vec<i32> = g.into_iter().collect();
        chars.sort_unstable();
        sorted_g.sort_unstable();
        for (i,&j) in (&sorted_g).iter().enumerate() {
            t[j as usize] = chars[i];
        }
    }
    for (i,c) in t.iter_mut().enumerate() {
        if *c == b'\0' { *c = b[i]; }
    }
    std::str::from_utf8(t.as_slice()).expect("").to_owned()
}
fn main() {
    println!("{}", smallest_string_with_swaps("dcab".to_string(), vec![vec![0,3],vec![1,2]]));
    println!("{}", smallest_string_with_swaps("dcab".to_string(), vec![vec![0,3],vec![1,2],vec![0,2]]));
    println!("{}", smallest_string_with_swaps("cba".to_string(), vec![vec![0,1],vec![1,2]]));
    println!("{}", smallest_string_with_swaps("dcab".to_string(), vec![]));
    println!("{}", smallest_string_with_swaps("vbjjxgdfnru".to_string(), vec![vec![8,6],vec![3,4],vec![5,2],vec![5,5],vec![3,5],vec![7,10],vec![6,0],vec![10,0],vec![7,1],vec![4,8],vec![6,2]]));
    println!("{}", smallest_string_with_swaps("wiftyfgoqfohnzelum".to_string(), vec![vec![3,2],vec![6,2],vec![9,11],vec![2,3],vec![5,4],vec![2,2],vec![4,3],vec![9,3],vec![10,0],vec![4,16],vec![5,8],vec![14,5],vec![4,16],vec![17,1],vec![9,7],vec![12,9],vec![1,17],vec![16,7]]));
}
