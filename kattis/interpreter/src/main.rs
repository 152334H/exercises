use std::io;
type Ins = (usize, usize, usize);
fn to_word(i: Ins) -> usize {
    i.0*100 + i.1*10 + i.2
}
fn from_word(w: usize) -> Ins {
    (w/100, (w%100)/10, w%10)
}
fn main() {
    let mut ram: [Ins;1000] = [(0,0,0);1000];
    for i in 0..1000 {
        let mut s = String::new();
        if let Ok(len) = io::stdin().read_line(&mut s) {
            if len < 3 { break; } 
            let mut it = s.chars();
            macro_rules! nextc { () => {
                it.next().unwrap() as usize - '0' as usize
            }}
            ram[i] = (nextc!(), nextc!(), nextc!());
        } else { break; }
    }
    let mut rip = 0;
    let mut reg = [0;10];
    for i in 0..10000 {
        let ins = ram[rip];
        match ins.0 {
            1 => { println!("{}", 1+i); break },
            2 => reg[ins.1] = ins.2,
            3 => reg[ins.1] += ins.2,
            4 => reg[ins.1] *= ins.2,
            5 => reg[ins.1] = reg[ins.2],
            6 => reg[ins.1] += reg[ins.2],
            7 => reg[ins.1] *= reg[ins.2],
            8 => reg[ins.1] = to_word(ram[reg[ins.2]]),
            9 => ram[reg[ins.2]] = from_word(reg[ins.1]),
            0 => if reg[ins.2] != 0 {
                rip = reg[ins.1]-1;
            }, _ => ()
        }
        reg[ins.1] %= 1000;
        rip += 1;
    }
}
