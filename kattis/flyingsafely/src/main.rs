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
    let t = to_int(&gets());
    for _ in 0..t {
        // this is a trick question, asking for the total length of an MST where all weights are 1.
        let tmp = get_vec_of_ints();
        let (n,m) = (tmp[0], tmp[1]);
        for __ in 0..m { gets(); }
        println!("{}", n-1);
        // The obvious answer is that, because all trees have N-1 edges, the length is N-1.
    }
}
