const inputEl = document.querySelector("textarea");
const submitEl = document.querySelector("button");

function getDigits (input) {
    let num = Math.abs(parseInt(input));
    let digits = 0;

    for (digits = 0; num > 0; digits++) {
        num = Math.floor(num / 10);
    }

    return digits
}




submitEl.addEventListener("click", ()=>{
    const input = inputEl.value;
    alert(`There are ${getDigits(input)} digits in the number ${input}`);
});