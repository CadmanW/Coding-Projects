use std::io;

struct Item {
    name: String,
    cost: u32,
}

struct User {
    name: String,
    bal: f32,
    inventory: Vec<Item>,
}

fn main() {

    let mut name = String::new();
    println!("What's your name?\n> ");
    io::stdin()
    
    
    let user = User {
        name: name,
        bal: 100.00,
        inventory: Vec::new(),
    };

}

// list things you can buy
//      
//
// get input to buy
//
// buy item
//
// repeat

/*
list things you can buy
    tuple
        name, price

get input to buy

buy item

repeat
*/