use std::io;
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s.trim().to_string();
}
fn to_int(s: &str) -> usize { s.parse().expect("to_int failure") }
fn main() {
    let n = to_int(&gets());
    let mut vac_c = 0;
    let mut vac_suc = [0;3];
    let mut ant_suc = [0;3];
    for _ in 0..n {
        let s = gets();
        let s = s.trim().as_bytes();
        let is_vac = s[0] == 'Y' as u8;
        if is_vac { vac_c += 1; }
        let r = if is_vac { &mut vac_suc } else { &mut ant_suc};
        for i in 0..3 { r[i] += (s[i+1] == 'Y' as u8) as i32 }
    }
    for i in 0..3 {
        let v_inf = vac_suc[i] as f64/vac_c as f64;
        let a_inf = ant_suc[i] as f64/(n-vac_c) as f64;
        if v_inf < a_inf {
            println!("{}", 100.0*(1.0-v_inf/a_inf));
        } else {
            println!("Not Effective");
        }
    }
}
