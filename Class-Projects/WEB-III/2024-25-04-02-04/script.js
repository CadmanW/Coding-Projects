const inputEl = document.querySelector("input");
const svg = document.querySelector("svg");

inputEl.addEventListener("blur", e => {
    document.querySelectorAll(".ball").forEach(e => e.remove());

    for (let i = 0; i < inputEl.value; i++) {
        const ball = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        ball.setAttribute("class", "ball");
        ball.setAttribute("cx", "50");
        ball.setAttribute("cy", "50");
        ball.setAttribute("r", "25");

        svg.appendChild(ball);
    }
});