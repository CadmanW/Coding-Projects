const svg = document.querySelector("svg");

initPlinkoBoard(200, 200, 25, 2);









function initPlinkoBoard(x, y, pegRadius, pegSpacing) {

    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg")
    svg.setAttribute("viewbox", `0 0 ${x} ${y}`);
    svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
    svg.setAttribute("width", x);
    svg.setAttribute("height", y);

    const pegX = (x / pegRadius) + (pegRadius * pegSpacing);
    const pegY = (x / pegRadius) + (pegRadius * pegSpacing);

    for (let y = 0; y < pegY; y++) {
        for (let x = 0; x < pegX; x++) {
            const peg = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            peg.setAttribute("fill", "#181818");
            peg.setAttribute("stroke", "#eee");
            peg.setAttribute("stroke-width", "3px");
            /*
            Math for getting X and Y:
                (pegRadius * x) gets the initial X coord for the circle
                (x * (pegSPacing * pegRadius)) gets the spacing between the pegs
                + pegRadius moves it a little over so it's not clipping out of the
            */

            peg.setAttribute("cx", `${parseInt((pegRadius * x) + (x * (pegSpacing * pegRadius)) + pegRadius)}px`);
            peg.setAttribute("cy", `${parseInt((pegRadius * y) + (y * (pegSpacing * pegRadius)) + pegRadius)}px`);
            peg.setAttribute("r", pegRadius);

            svg.appendChild(peg);
        }
    }

    document.body.append(svg);
}
