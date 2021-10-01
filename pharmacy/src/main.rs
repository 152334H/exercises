use std::io;
use std::collections::{BinaryHeap,VecDeque};
use std::cmp::Reverse;
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
    let tmp = get_vec_of_ints();
    let (n,t) = (tmp[0], tmp[1]);
    let mut orders = VecDeque::new();
    for _ in 0..n {
        let tmp = gets();
        let mut tmp = tmp.split(' ');
        orders.push_back((to_int(tmp.next().unwrap()),
                          tmp.next().unwrap()=="R",
                          to_int(tmp.next().unwrap())));
    }
    let mut time = orders[0].0;
    let mut current = BinaryHeap::new();
    let mut techies = BinaryHeap::new();
    let mut completion_time = [Vec::new(), Vec::new()];
    // this code is an unmaintainable mess. Read the python version if you want to understand it.
    macro_rules! update_time { ($to:expr) => {
        time = $to;
        while !orders.is_empty() && orders[0].0 <= time {
            let order = orders.pop_front().unwrap();
            current.push(Reverse((order.1, order.0, order.2)));
        }
    }}
    while !(orders.is_empty() && current.is_empty()) {
        if current.is_empty() { update_time!(orders[0].0); }
        let Reverse(nxt) = current.pop().unwrap();
        techies.push(Reverse((time+nxt.2, nxt.1, nxt.0)));
        while !techies.is_empty() &&
          (techies.peek().unwrap().0.0 <= time || techies.len() == t) {
            let Reverse(done) = techies.pop().unwrap();
            if done.0 > time { update_time!(done.0); }
            completion_time[done.2 as usize].push(done.0-done.1);
        }
    }
    for Reverse(done) in techies {
        completion_time[done.2 as usize].push(done.0-done.1);
    }
    println!("{}", completion_time.iter().map(|v|
                     if v.len() == 0 { 0 as f64 } else {
                       v.iter().sum::<usize>() as f64 / v.len() as f64
                     }).map(|f| f.to_string()).collect::<Vec<String>>()
                   .join(" "));
}
