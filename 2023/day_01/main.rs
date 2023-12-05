mod read;

use read::read;

fn main() {
    let input = read("input.txt");

    // valid words that should be mapped to its corresponding digits [1, 2, 3, ...]
    let mappings = vec![
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    ];

    // accumulators for the result of part1 and part2
    let mut sum1 = 0;
    let mut sum2 = 0;

    // goes through the input string line by line
    for line in input.lines() {
        // array to store digits to digtis
        let mut digits_num = Vec::<char>::new();
        // array to store both words to digits and digits to digits
        let mut digits_word = Vec::<char>::new();

        // goes throught the line character by character
        for (i, ch) in line.chars().enumerate() {
            // directly adding to array if its a digit
            if ch.is_digit(10) {
                digits_num.push(ch);
                digits_word.push(ch);
            } else {
                // checking for the valid words in the line
                for (val, word) in mappings.iter().enumerate() {
                    // extract the overlapping words
                    // such as: eightwo
                    // which should be consider as [8,2]
                    if line[i..].starts_with(word) {
                        // note: val + 1 is used to push - '1' if 'one' is found
                        digits_word.push(char::from_digit((val + 1) as u32, 10).unwrap());
                    }
                }
            }
        }

        // merge the first and last digits from the arrays
        // and adds it to the sum variables.

        //   -   sum1 - only digits
        sum1 += format!("{}{}", digits_num[0], digits_num[digits_num.len() - 1])
            .parse::<i32>()
            .unwrap();

        //   -   sum2 - digits and also words that are converted to digits
        sum2 += format!("{}{}", digits_word[0], digits_word[digits_word.len() - 1])
            .parse::<i32>()
            .unwrap();
    }

    println!("{}", sum1);
    println!("{}", sum2);
}
