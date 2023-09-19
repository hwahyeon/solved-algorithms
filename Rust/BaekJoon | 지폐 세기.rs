use std::io;

fn main() {
    let mut total = 0;

    let mut n = String::new();
    io::stdin().read_line(&mut n).expect("Failed to read line");
    let n: u32 = n.trim().parse().expect("Please enter a number");

    for _ in 0..n {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read line");
        let vec: Vec<u32> = input
            .trim()
            .split_whitespace()
            .map(|s| s.parse().expect("Please enter a number"))
            .collect();

        let (r, _h) = (vec[0], vec[1]);

        match r {
            136 => total += 1000,
            142 => total += 5000,
            148 => total += 10000,
            154 => total += 50000,
            _ => {}
        }
    }

    println!("{}", total);
}
