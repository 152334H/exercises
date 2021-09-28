use std::io;
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s;
}
fn main() {
    let s = gets();
    let toint = |x: &str|  x.parse().expect("not an int");
    let n: usize = toint(s.trim());
    for i in 1..=n {
        let l = gets();
        let mut it = l.trim().split(' ').into_iter();
        it.next();
        let mut dataset: Vec<usize> = it.map(toint).collect();
        let mut count = 0;
        for j in 1..20 {
            for k in (0..j).rev() {
                if dataset[k] > dataset[k+1] {
                    dataset.swap(k,k+1);
                    count = count + 1;
                }
            }
        }
        println!("{} {}", i, count);
    }
}
