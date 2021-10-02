use std::io;
const INF: usize = 1<<63;
fn main() {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    let mut v: Vec<usize> = s.trim().as_bytes().iter().map(|&b| (b-'0' as u8) as usize).collect();
    let mut pos: [usize;3] = [INF;3];
    let mut count: usize = 0;
    for i in 0..v.len() {
        let b = v[i];
        if pos[b] == INF { pos[b] = i; }
        let &next = v.get(i+1).unwrap_or(&3);
        if next < b { // sorted wrong
            // swap `next` to the leftmost instance of `b`.
            v[i+1] = v[pos[b]]; 
            v[pos[b]] = next;
            count += i+1-pos[b];
            if pos[next] == INF { pos[next] = pos[b]; }
            pos[b] += 1;
            if b-next == 2 && pos[1] != INF {
                // At this point, `next` is at where the last 1 should be.
                // swap `next` with the leftmost instance of 1.
                count += pos[2]-1-pos[1];
                v[pos[1]] = next;
                v[pos[2]-1] = 1;
                pos[1] += 1;
            }
        }
    }
    println!("{}", count);
}
