const inputEl = document.querySelector("#input");
const formEl = document.querySelector("#form");
const outputEl = document.querySelector("#output");

// The value of the MAX SAFE INTEGER constant is 9007199254740991 (9,007,199,254,740,991 or nine quadrillion)
const translate = {
    symbols: {
        "*": "times",
        "/": "divided-by",
        "+": "plus",
        "-": "minus",
        ".": "point",
        "^": "to-the-power-of"
    },

    allowedChars: [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",

        "*", "/", "+", "-", ".", ",", "^", " "
    ],

    numWords: {  
        "0": "", 
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",        
        "9": "nine"
    },

    bigWords: [
        "thousand",
        "million",
        "billion",
        "trillion",
        "quadrillion"
    ]
}


function output (str) {
    outputEl.innerText = str;
}


function validateInput (input) {
    // If input is just a finite number, return it as a string
    if (Number.isFinite(Number(input))) return input;

    // For every char make sure it's in the list of allowedChars, return invalid if not char not in list of allowedChars
    for (let i in input) {
        if (!translate.allowedChars.includes(input[i])) return "invalid";
    }

    // If input is valid and not just numbers, strip all numbers and commas
    return input.replace(" ", "").replace(",", "");
}


function seperateExpression (expression) {

    // For the length of expression (to make sure we get every symbol) try to translate every symbol to its word counterpart
    for (let i in expression) {
        for (let symbol in translate.symbols) {
            expression = expression.replace(symbol, ` ${translate.symbols[symbol]} `);
        }
    }

    // Splits the expression into numbers and words
    return expression.split(" ");
}


function translateNumbers (nums) {

    let subNums = [];

    

}


function translateExpression(expression) {

    const subExpressions = seperateExpression(expression);
    let finalExpression = "";

    // For every subExpression, if it is a number, translate the numbers to words and add that to fnal string
    // Else, add the non-number string to the finalExpression
    for (let i in subExpressions) {
        if (Number.isFinite(Number(subExpressions[i]))) {
            finalExpression += `${translateNumbers(subExpressions[i])} `;
        }
        else {
            finalExpression += `${subExpressions[i]} `;
        }
    }

    return finalExpression.trim();
}






// This code block runs everytime there is an input into the form
formEl.addEventListener("input", () => {
    // If input is invalid, output invalid, else output the translated expression
    const input = validateInput(inputEl.value);
    input === "invalid" ? output("Invalid Input") : output(translateExpression(input)); 
});