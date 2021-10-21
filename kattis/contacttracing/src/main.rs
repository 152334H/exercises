use std::io;
use std::collections::{HashMap,HashSet};
fn gets() -> String {
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("gets error");
    return s.trim().to_string();
}
fn to_int(s: &str) -> usize { s.parse().expect("to_int failure") }
fn get_vec_of_ints() -> Vec<usize> {
    gets().split(' ').map(to_int).collect()
}
fn main() {
    /* summary: sort the ranges by time,
     * build a graph of connected people,
     * and do a cycle of BFS for every D.
     * This method will be EXTREMELY SLOW for a highly-connected graph,
     * but evidently the problem doesn't contain dense graphs beacuse
     * this solution easily AC'd.
     * See `0.in` for a test case where this solution will be very slow.
     */
    let tmp = get_vec_of_ints();
    let (n,d) = (tmp[0], tmp[1]);
    let tmp = gets();
    let mut it = tmp.split(' ').map(to_int);
    it.next().unwrap();
    let mut infected = it.collect::<Vec<usize>>();

    // read the timeline
    let mut events = Vec::new();
    for i in 1..=n {
        let tmp = get_vec_of_ints();
        let (start,end) = (tmp[0], tmp[1]);
        events.push((start,false,i));
        events.push((end,true,i)); // ergo, end will appear after start.
    }
    events.sort();

    // now build the graph.
    let mut adjls: HashMap<usize,Vec<usize>> = (1..=n)
        .map(|i| (i,Vec::new())).collect();
    let mut people = HashSet::<usize>::new();
    for (_,is_end,i) in events {
        if is_end {
            people.remove(&i);
        } else {
            for p in &people {
                adjls.get_mut(p).unwrap().push(i);
                adjls.get_mut(&i).unwrap().push(*p);
            }
            people.insert(i);
        }
    }

    // now BFS.
    let mut seen: HashSet<usize> = infected.clone().into_iter().collect();
    for _ in 0..d { 
        let mut new_inf = Vec::new();
        for inf in &infected {
            for oth in &adjls[inf] {
                if !seen.contains(oth) {
                    seen.insert(*oth);
                    new_inf.push(*oth);
                }
            }
        }
        infected = new_inf;
    }

    let mut res: Vec<usize> = seen.into_iter().collect();
    res.sort();
    let res: Vec<String> = res.into_iter().map(|x| x.to_string()).collect();
    println!("{}", res.join(" "));
}
