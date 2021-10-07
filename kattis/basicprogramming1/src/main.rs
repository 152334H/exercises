use std::io;
use std::collections::{HashMap,BinaryHeap,HashSet};
use std::cmp::Ordering;
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s.trim().to_string();
}
fn to_int(s: &str) -> usize { s.parse().expect("to_int failure") }
fn get_vec_of_ints() -> Vec<usize> {
    gets().split(' ').map(to_int).collect()
}
fn main() {
    let arr = get_vec_of_ints();
    let (n,t) = (arr[0], arr[1]);
    let mut arr = get_vec_of_ints();
    match t {
        1 => println!("7"),
        2 => println!("{}", match arr[0].cmp(&arr[1]) {
            Ordering::Greater => "Bigger",
            Ordering::Equal => "Equal",
            Ordering::Less => "Smaller"
        }),
        3 => {
            let three = &mut arr[0..3];
            three.sort();
            println!("{}", three[1]);
        },
        4 => println!("{}", arr.iter().sum::<usize>()),
        5 => println!("{}", arr.iter().filter(|&&v| v%2==0).sum::<usize>()),
        6 => println!("{}", arr.iter().map(|v| (v%26+('a' as usize)) as u8 as char).collect::<String>()),
        7 => println!("{}", {
            let mut i = 0;
            let mut seen = HashSet::new();
            loop {
                if seen.contains(&i) { break "Cyclic" }
                seen.insert(i);
                i = arr[i];
                if !(0..n).contains(&i) { break "Out" }
                else if i == n-1 { break "Done" }
            }
        }),
        _ => ()
    }

}
