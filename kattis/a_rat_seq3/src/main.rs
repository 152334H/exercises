use std::io;
use std::collections::HashMap;
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s.trim().to_string();
}
fn to_int(s: &str) -> usize { s.parse().expect("to_int failure") }
fn get_vec_of_ints() -> Vec<usize> {
    gets().split(' ').map(to_int).collect()
}
type Fract = (usize, usize);
fn bit_parse(mut n: usize) -> Vec<usize> {
    let mut ls = Vec::new();
    while n != 0 {
        ls.push(n&1);
        n >>= 1
    }
    ls
}
fn main() {
    let mut f: HashMap<usize,Fract> = HashMap::new();
    f.insert(0, (0,1)); // hidden root; F(1) is to the right of this.
    for k in 1..=to_int(&gets()) {
        let mut n = 0;
        let mut frac = f[&0];
        for &bit in bit_parse(get_vec_of_ints()[1]).iter().rev() {
            n = (n<<1)+bit;
            frac = *f.entry(n).or_insert_with(||
                if bit == 0 {
                    (frac.0, frac.0+frac.1) // left child is p/(p+q).
                } else {
                    (frac.0+frac.1, frac.1) // right child is (p+q)/q.
            });
        }
        println!("{} {}/{}", k, frac.0, frac.1);
    }

}
