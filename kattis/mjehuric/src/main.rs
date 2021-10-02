use std::io;
fn bubblesort(arr: &mut Vec<u32>) {
    loop {
        let mut sorted = true;
        for i in 0..arr.len()-1 {
            if arr[i] > arr[i+1] {
                sorted = false;
                arr.swap(i,i+1);
                println!("{}", arr.iter().map(|x| x.to_string()).collect::<Vec<String>>().join(" "));
            }
        }
        if sorted { return; }
    }
}
fn main() {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("");
    let mut input: Vec<u32> = s.trim().split(' ').map(|x| x.parse().expect("")).collect();
    bubblesort(&mut input);
}
