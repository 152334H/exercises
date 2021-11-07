pub struct Solution {}
const BASE: u8 = 10;
impl Solution {
    pub fn multiply(num1: String, num2: String) -> String {
        let num1 = num1.into_bytes();
        let num2 = num2.into_bytes();
        let mut res = vec![0; num1.len() + num2.len()];
        for (i,&a) in num1.iter().rev().enumerate() {
            for (j,&b) in num2.iter().rev().enumerate() {
                let mut tmp = (a-b'0') * (b-b'0');
                let mut idx = i + j;
                while tmp > 0 {
                    tmp += res[idx];
                    res[idx] = tmp%BASE;
                    tmp /= BASE;
                    idx += 1;
                }
            }
        }
        match res.iter().rev().position(|&x| x != 0) {
            Some(first_nonzero) => res[..res.len()-first_nonzero]
                .iter().rev().map(|&x| (x+b'0') as char).collect(),
            None => "0".to_string() // edge case: answer is 0
        }
    }
}
