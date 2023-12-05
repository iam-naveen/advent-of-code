use std::{fs::File, io::Read};

pub fn read(path: &str) -> String {
    let mut file = match File::open(path) {
        Ok(content) => content,
        Err(why) => panic!("Reason: {}", why),
    };

    let mut s = String::new();

    match file.read_to_string(&mut s) {
        Ok(content) => content,
        Err(why) => panic!("{}", why),
    };

    s
}
