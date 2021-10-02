use std::io;
use std::collections::HashSet;
const MMAX: usize = 500001;
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s.trim().to_string();
}
fn to_int(s: &str) -> usize { s.parse().expect("to_int failure") }
fn get_ingredients() -> Vec<usize> {
    gets().split(' ').skip(1).map(to_int).collect()
}
fn findset(parent: &mut [usize;MMAX], x: usize) -> usize {
    if parent[x] == x { x } else {
        parent[x] = findset(parent, parent[x]);
        parent[x]
    }
}
fn main() {
    let mut parent: [usize;MMAX] = [0;MMAX];
    let mut lens: [usize;MMAX] = [1;MMAX];
    macro_rules! findset {
        ($x:expr) => { findset(&mut parent, $x) };
    }
    let n = to_int(&gets());
    for i in 0..MMAX { parent[i] = i; }
    let mut count = 0;
    for _ in 0..n {
        let recipe = get_ingredients();
        let groups: HashSet<usize> = recipe.iter().map(|&x| findset!(x)).collect();
        //println!("{:?} || {:?} || {:?}", recipe, groups, &lens[0..=5]);
        if groups.iter().map(|&g| lens[g]).sum::<usize>() == recipe.len() {
            groups.into_iter().reduce(|x: usize, y: usize| {
                let (a,b) = (findset!(x), findset!(y));
                if a != b {
                    parent[b] = a;
                    lens[a] += lens[b];
                }; a
            }); // reduce by union
            count += 1;
        }
    }
    println!("{}", count);
}
