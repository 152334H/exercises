/* the code here is 100% correct. But it performs a lot worse than the cpp version.
 * Possible explanations:
     * vector indexing && object access is slower than static arrays.
     * unknown implementation differences
 */
use std::io;
use std::mem::swap;
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s.trim().to_string();
}
fn to_int(s: &str) -> usize { s.parse().expect("to_int failure") }
fn get_vec_of_ints() -> Vec<usize> {
    gets().split(' ').map(to_int).collect()
}
struct ufds {
    parent: Vec<usize>,
    rank: Vec<usize>
}
impl ufds {
    fn new(sz: usize) -> ufds {
        ufds {
            parent: (0..sz).collect(),
            rank: vec![0;sz]
        }
    }
    fn findset(&mut self, mut a: usize) -> usize {
        while self.parent[a] != a { // idk i copied this from wikipedia
            self.parent[a]  = self.parent[self.parent[a]];
            a = self.parent[a];
        }
        a
    }
    fn union(&mut self, a: usize, b: usize) {
        let (mut x, mut y) = (self.findset(a), self.findset(b));
        if x != y { // now with union by rank. Hopefully properly this time.
            if self.rank[x] < self.rank[y] {
                swap(&mut x, &mut y);
            }
            self.parent[y] = x;
            self.rank[x] += self.rank[y];
        }
    }
}
fn main() {
    let tmp = get_vec_of_ints();
    let (n,q) = (tmp[0], tmp[1]);
    let mut sets = ufds::new(n);

    for _ in 0..q {
        let line = gets();
        let mut query = line.split(' ');
        let op = query.next().unwrap();
        let (a,b) = (to_int(query.next().unwrap()),
                     to_int(query.next().unwrap()));
        match op {
            "?" => { // query
                println!("{}", if sets.findset(a) == sets.findset(b) { "yes" } else { "no" });
            },
            "=" => { // union
                sets.union(a,b);
            }, _ => ()
        }
    }
}
