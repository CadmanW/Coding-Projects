const svg = document.querySelector("svg");

initPlinkoBoard(
    pegRadius = 50,
    pegSpacing = 1,
    pegColor = "black",
    pegX = 10,
    pegY = 10
);










function initPlinkoBoard(pegRadius, pegSpacing, pegColor, pegX, pegY) {
    for (let y = 0; y < pegY; y++) {
        for (let x = 0; x < pegX; x++) {
            const peg = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            peg.setAttribute("fill", pegColor);
            /*
            Math for getting X and Y:
                (pegRadius * x) gets the initial X coord for the circle
                
            */

            peg.setAttribute("cx", `${parseInt((pegRadius * x) + (x * (pegSpacing * pegRadius)) + pegRadius)}px`);
            peg.setAttribute("cy", `${parseInt((pegRadius * y) + (y * (pegSpacing * pegRadius)) + pegRadius)}px`);
            peg.setAttribute("r", pegRadius);

            svg.appendChild(peg);
        }
    }
}
