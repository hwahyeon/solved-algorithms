use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let t: i32 = input.trim().parse().unwrap();

    for _ in 0..t {
        let mut line = String::new();
        io::stdin().read_line(&mut line).unwrap();
        let parts: Vec<i32> = line.trim().split_whitespace()
                                  .map(|s| s.parse().unwrap())
                                  .collect();

        let ai = parts[0];
        let bi = parts[1];
        let xi = parts[2];

        println!("{}", ai * (xi - 1) + bi);
    }
}
