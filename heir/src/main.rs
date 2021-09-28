use std::io;
fn valid_combi(val: usize) -> bool {
    let mut arr = [false; 10];
    let mut v = val;
    while v != 0 {
        let last: usize = v%10;
        v = v/10;
        if arr[last] || last == 0 || val%last != 0 {
            return false;
        }
        arr[last] = true;
    }
    true
}
fn main() {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("");
    let v: Vec<usize> = s.trim().split(' ').
        map(|x| x.parse().expect("")).collect();
    println!("{}", (v[0]..=v[1]).filter(|x| valid_combi(*x)).count());
}
