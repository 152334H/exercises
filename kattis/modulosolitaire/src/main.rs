use std::io;
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
    let (m,n,s0) = (tmp[0], tmp[1], tmp[2]);
    let ab = (0..n).map(|_| {
        let s = gets();
        let mut it = s.split(' ').map(to_int);
        (it.next().unwrap(), it.next().unwrap())
    }).collect::<Vec<_>>();
    let mut border = vec![s0];
    let mut vis = [false; 1000001];
    for i in 0..usize::MAX {
        let mut nb = vec![];
        for &s in border.iter() {
            if s == 0 { return println!("{}", i); }
            for &(a,b) in ab.iter() {
                let ns = (s*a+b)%m;
                if !vis[ns] {
                    vis[ns] = true;
                    nb.push(ns);
                }
            }
        }
        if nb.is_empty() { return println!("-1"); }
        border = nb;
    }
}
