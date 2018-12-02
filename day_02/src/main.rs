use std::fs;
use std::collections::HashMap;

fn main() {
    let content = fs::read_to_string("input")
        .expect("Error opening file");

    let mut count2 = 0;
    let mut count3 = 0;

    for line in content.lines() {
        let mut char_count = HashMap::with_capacity(26);

        for char in line.chars(){
            *char_count.entry(char).or_insert(0) += 1;
        }

        if char_count.values().any(|&count| count == 2) {
            count2 += 1
        }

        if char_count.values().any(|&count| count == 3) {
            count3 += 1
        }
    }

    println!("{} * {} = {}", count2, count3, count2 * count3);

    println!("-------------");
    let mut box_id: Vec<char> = Vec::new();

    for (idx, line1) in content.lines().enumerate() {
        for line2 in content.lines().skip(idx + 1) {
            if line1.chars().zip(line2.chars()).filter(|(a, b)| a != b).count() == 1 {
                // return word with missing pos
                box_id = line1
                    .chars()
                    .zip(line2.chars())
                    .filter(|(a,b)| a == b)
                    .map(|(a, _)| a)
                    .collect();
            }
        }
    }

    let box_id: String = box_id.into_iter().collect();

    println!("Common letters of the corrext box_ides: {}", box_id);
}