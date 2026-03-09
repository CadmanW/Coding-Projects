use std::io;

// Scrambles password entered using XOR with 0x5A (Z in ascii)
fn scramble(input: &str) -> Vec<u8> {
    input.bytes().map(|b| b ^ 0x5A).collect()
}

// Decodes the flag
fn decode_flag(encoded: &[u8]) -> String {
    encoded.iter().map(|&b| (b ^ 0x5A) as char).collect()
}

fn main() {
    let scrambled_password: &[u8] = &[
        0x1A, 0x2B, 0x3E, 0x3E, 0x21, 0x6B, 0x79, 0x69,
        0x1A, 0x79, 0x6B, 0x21, 0x7B, 0x21, 0x69, 0x79,
    ];

    // Flag also XOR'd with 0x5A - won't appear in strings view
    let encoded_flag: &[u8] = &[
        0x0E, 0x0E, 0x0F, 0x21, 0x2A, 0x6E, 0x29, 0x29, 
        0x2D, 0x6A, 0x28, 0x3E, 0x05, 0x32, 0x6E, 0x39, 
        0x31, 0x69, 0x3E, 0x27,
    ];

    println!("Enter password:");
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");

    let input = input.trim();
    let scrambled_input = scramble(input);

    if scrambled_input == scrambled_password {
        let flag = decode_flag(encoded_flag);
        println!("Access granted! Flag: {}", flag);
    } else {
        println!("Access denied!");
    }
}

// @qdd{1#3@#1{!{3#