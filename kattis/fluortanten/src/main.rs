use std::io;
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s.trim().to_string();
}
fn to_int(s: &str) -> i64 { s.parse().expect("to_int failure") }
fn get_vec_of_ints() -> Vec<i64> {
    gets().split(' ').map(to_int).collect()
}
fn main () {
    let n = to_int(&gets());
    let ls = get_vec_of_ints();
    let mut zero_seen = 0;
    let mut ma = ls.iter().enumerate().map(|(i,&v)| {
        if v == 0 { zero_seen = 1; }
        (i+2-zero_seen) as i64*v
    }).sum::<i64>();
    let mut total = ma;
    for v in ls {
        if v != 0 {
            total -= v;
            ma = ma.max(total);
        }
    }
    println!("{}", ma);
}
