use std::fs;
use std::collections::HashSet;

fn main() {
    let content = fs::read_to_string("input")
        .expect("Error opening file");

    let mut frequency = 0;
    for line in content.lines() {
        frequency += &line.parse::<i32>().unwrap();
    }
    println!("Final frequency: {}", frequency);

    println!("-------------");

    frequency = 0;
    let mut seen_frequencies = HashSet::new();

    'outer: loop {
        for line in content.lines() {
            frequency += &line.parse::<i32>().unwrap();
            let repeated = seen_frequencies.insert(frequency);
            if !repeated {
                break 'outer;
            }
        }
    }
    println!("\nFirst frequency reached twice: {}", frequency);
}