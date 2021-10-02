use std::io;
use std::collections::HashSet;
fn main() {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("");
    let mut nums: HashSet<u32> = HashSet::new();
    for sub in s.trim().split(';') {
        if sub.find('-') == None {
            nums.insert(sub.parse().expect("fuck1"));
        } else {
            let v: Vec<u32> = sub.split('-').into_iter()
                .map(|x| x.parse().expect("fuck")).collect();
            for i in v[0]..=v[1] {
                nums.insert(i);
            }
        }
    }
    println!("{}", nums.len());
}
