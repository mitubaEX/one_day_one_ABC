use std::io::Read;
// ai = ai+2
fn main() {
    let mut buf = String::new();
    std::io::stdin().read_to_string(&mut buf).unwrap();

    let mut iter = buf.split_whitespace();

    let n: usize = iter.next().unwrap().parse().unwrap();
    println!("{}", n);

    let lrt: Vec<i64> = (0..n).map(|_| iter.next().unwrap().parse().unwrap()).collect();

    println!("{:?}", lrt);
    let odd: Vec<i64> = &lrt.into_iter().filter(|x| x % 2 != 0).collect();

    println!("{:?}", odd);

    let even: Vec<i64> = &lrt.into_iter().filter(|x| x % 2 == 0).collect();

    println!("{:?}", even);
}
