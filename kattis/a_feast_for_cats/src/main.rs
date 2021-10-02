use std::io;
//  use std::convert::TryInto;
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s.trim().to_string();
}
fn to_int(s: &str) -> usize { s.parse().expect("to_int failure") }
fn get_vec_of_ints() -> Vec<usize> {
    gets().split(' ').map(to_int).collect()
}
const CMAX: usize = 2001;
fn main() {
    let mut parent: [usize; CMAX] = [0; CMAX];
    fn findset(ufds: &mut [usize], x: usize) -> usize {
        if ufds[x] == x { x } else {
            ufds[x] = findset(ufds, ufds[x]);
            ufds[x]
        }
    }
    macro_rules! findset {
        ($x:expr) => {
            findset(&mut parent, $x)
        };
    }
    for _t in 0..to_int(&gets()) {
        let tmp = get_vec_of_ints();
        let m = tmp[0];
        let c = tmp[1];
        for (i,p) in parent.iter_mut().enumerate() {
            *p = i;
        }
        let mut edges = Vec::new();
        for _ in 0..c*(c-1)/2 {
            let tmp = get_vec_of_ints();
            edges.push((tmp[2], tmp[0], tmp[1]));
        }
        edges.sort();
        let mut total = c;
        for (d,i,j) in edges {
            let a = findset!(i);
            let b = findset!(j);
            if a != b {
                total += d;
                parent[b] = a;
            }
        }
        println!("{}", if total > m { "no" } else { "yes" });
        
    }
}
