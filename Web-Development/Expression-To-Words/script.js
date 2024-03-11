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

    numbers: {  
        "1": " one",
        "2": " two",
        "3": " three",
        "4": " four",
        "5": " five",
        "6": " six",
        "7": " seven",
        "8": " eight",        
        "9": " nine"
    },

    tensNumbers: {
        "2": "twenty",
        "3": "thirty",
        "4": "forty",
        "5": "fifty",
        "6": "sixty",
        "7": "seventy",
        "8": "eighty",
        "9": "ninety"
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
    if (Number.isFinite(Number(input))) {
        return input;
    }

    // For every char make sure it's in the list of allowedChars, return invalid if not char not in list of allowedChars
    for (let i in input) {
        if (!translate.allowedChars.includes(input[i])) {
            return "invalid";
        }
    }

    // If input is valid and not just numbers, strip all numbers and commas
    return input.replace(" ", "").replace(",", "");
}


function seperateExpression (expression) {

    // For the length of expression (to make sure we get every symbol) try to translate every symbol to its word counterpart
    for (let i = 0; i < expression.length; i++) {
        for (let symbol in translate.symbols) {
            expression = expression.replace(symbol, ` ${translate.symbols[symbol]} `);
        }
    }

    // Removes the white space at the ends of expression then splits the expression into groups of numbers and the symbol words in an array
    return expression.trim().split(" ");
}


function translateNumbers (nums) {

    // Group the numbers into items that have a length of three in an array to represent common math formatting big numbers using commas (1234567 > 1,234,567)
    let numGroups = [];
    let firstGroupLength = nums.length % 3;
    let finalString = [];

    // Get the first group length so that 12345 outputs to 12,345 instead of 123,45
    if (firstGroupLength === 0) {
        firstGroupLength = 3;
    }

    // Add the numbers from digits 1 to firstGroupLength from nums to numGroups
    numGroups[numGroups.length] = nums.slice(0, firstGroupLength);

    // Starting at firstGroupLength digit in nums, add 3 digits as an item to numGroups array until all numbers are added as groups
    for (let i = firstGroupLength; i < nums.length; i += 3) {
        numGroups[numGroups.length] = nums.slice(i, i + 3);
    }

    // Iterate through the array of groups of numbers
    for (let a = 0; a < numGroups.length; a++) {

        const group = numGroups[a];

        // Iterate through each number in the group
        for (let i = 0; i < group.length; i++) {

            let num = group[i];

            // Skip all zeros
            if (num != 0) {
                // Translate number to its word
                finalString[finalString.length] = `${translate.numbers[num]}`;

                // If it's the first digit in the group and the group is 3 digits long, add hundred to finalString
                if (group.length === 3 && i === 0) {
                    finalString[finalString.length] = "hundred";
                }

                // If it's the first digit and group length is 2; or second digit and group length is 3: then add the tens place word in place of the last number words
                if ((group.length === 2 && i === 0) || (group.length === 3 && i === 1)) {

                    // For the "teen" numbers
                    if (num == 1) {
                        num = group[++i];

                        switch (num) {
                            case "0":
                                finalString[finalString.length - 1] = "ten";
                                break;

                            case "1":
                                finalString[finalString.length - 1] = "eleven";
                                break;

                            case "2":
                                finalString[finalString.length - 1] = "twelve";
                                break;

                            case "3":
                                finalString[finalString.length - 1] = "thirteen";
                                break;

                            case "4":
                                finalString[finalString.length - 1] = "fourteen";
                                break;

                            case "5":
                                finalString[finalString.length - 1] = "fifteen";
                                break;

                            case "6":
                                finalString[finalString.length - 1] = "sixteen";
                                break;

                            case "7":
                                finalString[finalString.length - 1] = "seventeen";
                                break;

                            case "8":
                                finalString[finalString.length - 1] = "eighteen";
                                break;

                            case "9":
                                finalString[finalString.length - 1] = "nineteen";
                                break;
                        }
                    } else {
                        finalString[finalString.length - 1] = `${translate.tensNumbers[num]}`;
                    }
                }
            }
        }
        // After translating the numbers for the group, add the bigWord
        if (numGroups.length > 1) {
            const bigWord = translate.bigWords[numGroups.length - a - 2];

            if (bigWord !== undefined) {
                finalString[finalString.length] = bigWord;
            }
        }
    }

    // return the items in finalString joined as a string, seperated by a space
    return finalString.join(" ")
    
}


function translateExpression(expression) {

    const subExpressions = seperateExpression(expression);
    let finalExpression = [];

    // For every subExpression, if it is a number, translate the numbers to words and add that to final string
    // Else, add the non-number string to the finalExpression
    for (let i in subExpressions) {
        if (Number.isFinite(Number(subExpressions[i]))) {
            finalExpression[finalExpression.length] = translateNumbers(subExpressions[i]);
        }
        else {
            finalExpression[finalExpression.length] = subExpressions[i];
        }
    }

    // Remove the whitepspace at the ends of finalExpression
    return finalExpression.join(" ");
}






// This code block runs everytime there is an input into the form
formEl.addEventListener("input", () => {
    // If input is invalid, output invalid, else output the translated expression
    const input = validateInput(inputEl.value);
    input === "invalid" ? output("Invalid Input") : output(translateExpression(input)); 
});