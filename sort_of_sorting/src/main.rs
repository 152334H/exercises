use std::io;
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s.trim().to_string();
}
fn sort_by_index(arr: &mut [Option<&Vec<u8>>], ind: usize) {
    const INIT: Vec<&Vec<u8>> = Vec::new();
    let mut radix: [Vec<&Vec<u8>>; 128] = [INIT; 128];
    for t in arr.iter().enumerate() {
        let (_i, opt): (usize, &Option<&Vec<u8>>) = t;
        match opt {
            Some(r) => {
                radix[r[ind] as usize].push(r);
            },
            None => { break; }
        }
    }
    let mut i = 0;
    for v in radix.iter() {
        for r in v {
            arr[i] = Some(r);
            i = i+1;
        }
    }
}
fn main() {
    loop {
        let n: usize = gets().parse().expect("");
        if n == 0 { return; }
        let input: Vec<Vec<u8>> = (0..n).map(|_| gets().into_bytes()).collect();
        let mut mutv: [Option<&Vec<u8>>; 200] = [None; 200];
        for i in 0..n { mutv[i] = Some(&input[i]); }
        for i in (0..2).rev() { sort_by_index(&mut mutv, i); }
        for opt in mutv.iter() { 
            match opt {
                Some(r) => {
                    println!("{}", std::str::from_utf8(r).expect(""));
                },
                None => { println!(""); break; }
            }
        }

    }
}
