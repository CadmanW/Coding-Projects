const inputEl = document.querySelector("#input");
const formEl = document.querySelector("#form");
const outputEl = document.querySelector("#output");


function output (str) {
    outputEl.innerText = str;
}


function validateInput (input) {
    const allowedChars = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        
        "*", "/", "+", "-", ".", ",", "^", " "
    ]

    // If input is just a finite number, return it as a string
    if (Number.isFinite(input)) return String(input);

    // Go through every char and make sure it's in the list of allowedChars, return invalid if not char not in list of allowedChars
    for (let i = 0; i < input.length; i++) {
        if (!allowedChars.includes(input[i])) return "invalid";
    }

    // If input is valid and not just numbers, strip all numbers and commas
    return input.replace(" ", "").replace(",", "");
}


function seperateExpression (expression) {
    // The spaces in the word strings are so that the split method seperates the expression
    const symbols = {
        "*": " times ",
        "/": " divided-by ",
        "+": " plus ",
        "-": " minus ",
        ".": " point ",
        "^": " to-the-power-of "
    }

    // Go through every symbol and try to replace it in the expression with the word version
    for (let symbol in symbols) expression = expression.replace(symbol, symbols[symbol]);

    // Splits the expression into numbers and words
    return expression.split(" ");
}


function translateExpression(expression) {
    expression = seperateExpression(expression);
    console.log(expression);
}






// This code block runs everytime there is an input into the form
formEl.addEventListener("input", () => {
    // If input is invalid, output invalid, else output the translated expression
    const input = validateInput(inputEl.value);
    input === "invalid" ? output(`"${input}" is not a valid input`) : output(translateExpression(input)); 
});