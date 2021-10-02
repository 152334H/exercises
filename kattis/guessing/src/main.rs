use std::io;
use std::cmp::Ordering;
use rand::Rng;
fn main() {
    println!("Hello, world!");
    loop {
        println!("give a number: ");
        let mut guess = String::new();
        io::stdin().read_line(&mut guess)
            .expect("error reading line");
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("That was not a number");
                continue;
            }
        };
        let secret = rand::thread_rng().gen_range(1..101);
        println!("debug: guess == {}, secret == {}", guess, secret);
        match guess.cmp(&secret) {
            Ordering::Less => println!("lesser"),
            Ordering::Greater => println!("more"),
            Ordering::Equal => { 
                println!("ok");
                break;
            }
        };
    }
}
