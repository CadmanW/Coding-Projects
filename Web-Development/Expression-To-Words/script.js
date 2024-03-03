const inputEl = document.querySelector("#input");
const formEl = document.querySelector("#form");
const outputEl = document.querySelector("#output");

// Biggest possible number in JavaScript is 9,007,199,254,740,991 or nine quadrillion
const numbers = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    
    10: "ten",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",

    100: "hundered",
    1000: "thousand",
    1000000: "million",
    1000000000: "billion",
    1000000000000: "trillion",
    1000000000000000: "quadrillion"
}

const symbols = {
    "*": " times ",
    "/": " divided-by ",
    "+": " plus ",
    "-": " minus ",
    ".": " point ",
    "^": " to-the-power-of "
}




// Output
function output (str) {
    outputEl.innerText = str;
}

// Validates the user input
// If userInput is a number, return the number
// For every character in userInput, if it is not in the allowedChars array, then output "invalid string"
// If it passes the validation, return the input after deleting all spaces
function validateInput (userInput) {
    const allowedChars = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",

        "*",
        "/",
        "+",
        "-",
        ".",
        ",",
        "^",
        " "
    ]

    if (Number.isInteger(userInput)) return parseInt(userInput);

    for (let i = 0; i < userInput.length; i++) {
        if (!allowedChars.includes(userInput[i])) {
            output(`"${userInput}" is not a valid input`);
            return "invalid";
        }
    }

    return userInput.replace(" ", "").replace(",", "");
}

function numsToWords(expression) {
    // Changesall symbols to words
    for (i in expression) {    
        for (let i in symbols) {
            expression = expression.replace(i, symbols[i]);
        }
    }

    // Split the expression into parts of number and not numbers
    expression = expression.split(" ");

    return expression;
    
}

// This listens for any input in the input text box
formEl.addEventListener("input", () => {
    let validInput = validateInput(inputEl.value);

    if (validInput !== "invalid") output(numsToWords(validInput)); 
});