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
struct SegTree {
    n: usize,
    t: Vec<usize>
}
impl SegTree {
    fn new(ls: Vec<usize>) -> SegTree {
        let mut me = SegTree {
            n: ls.len(),
            t: vec![0;ls.len()]
        };
        me.t.extend(ls);
        for i in (1..me.n).rev() {
            me.t[i] = me.t[i<<1] + me.t[i<<1|1];
        }
        me
    }
    fn modify(&mut self, p: usize, v: usize) {
        let mut p = p + self.n;
        self.t[p] = v;
        while p > 1 {
            self.t[p>>1] = self.t[p] + self.t[p^1];
            p >>= 1;
        }
    }
    fn query(&mut self, l: usize, r: usize) -> usize {
        let mut res = 0;
        let mut l = l + self.n;
        let mut r = r + self.n;
        while l < r {
            if l&1 == 1 {
                res += self.t[l];
                l += 1;
            }
            if r&1 == 1 {
                r -= 1;
                res += self.t[r];
            }
            l >>= 1;
            r >>= 1;
        }
        res
    }
}

fn main() {
    let (_,q) = { let tmp = get_vec_of_ints(); (tmp[0], tmp[1]) };
    let mut vec_p = get_vec_of_ints();
    let mut vec_v: Vec<usize> = gets().trim().chars().map(|c| (c as u8 - '0' as u8 - 1) as usize).collect();
    let mut trees: Vec<SegTree> = (0..6).map(|i| SegTree::new(
                                 vec_v.iter().map(|&v| (v==i) as usize).collect()
                              )).collect();
    for _ in 0..q {
        let query = get_vec_of_ints();
        match query[0] {
            1 => {
                let (k,p) = (query[1]-1, query[2]-1);
                let orig_p = vec_v[k];
                vec_v[k] = p;
                trees[orig_p].modify(k,0);
                trees[p].modify(k,1);
            },
            2 => {
                let (p,v) = (query[1]-1, query[2]);
                vec_p[p] = v;
            },
            3 => {
                let (l,r) = (query[1]-1, query[2]);
                println!("{}", (0..6).map(|p| trees[p].query(l,r)*vec_p[p]).sum::<usize>());
            },
            _ => unreachable!()
        }
    }
}
