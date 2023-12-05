mod read;
use read::read;
use std::collections::HashMap;

fn main() {
    let input = read("input.txt");

    let valid_map = HashMap::from([("red", 12), ("green", 13), ("blue", 14)]);
    let mut res = 0;
    let mut res2 = 0;

    for (i, line) in input.lines().enumerate() {
        let sets = line.split(":").collect::<Vec<&str>>()[1];
        let game_id = (i + 1) as i32;

        let mut valid = true;
        let mut max_map = HashMap::from([("red", 0), ("green", 0), ("blue", 0)]);

        sets.split(";").for_each(|set| {
            set.split(",").for_each(|value| {
                let (count, color) = match value.trim().split(" ").collect::<Vec<&str>>()[..] {
                    [first, second] => (first.parse::<i32>().unwrap(), second),
                    _ => (0, ""),
                };
                if count > valid_map[color] {
                    valid = false
                }
                // changing the value in the hashmap
                match max_map.get_mut(color) {
                    Some(val) => *val = count.max(*val),
                    None => {}
                }
            })
        });
        if valid {
            res += game_id
        }
        let power = max_map.values().fold(1, |acc, val| acc * val);
        res2 += power
    }
    println!("Part 01 -> {}", res);
    println!("Part 02 -> {}", res2);
}
