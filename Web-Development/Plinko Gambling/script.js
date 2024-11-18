const svg = document.querySelector("svg");









function initPlinkoBoard(width, height, pegDiameter, pegSpacing) {
    // Create the SVG for the plinko board
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg")
    svg.setAttribute("viewbox", `0 0 ${width} ${height}`);
    svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
    svg.setAttribute("width", width);
    svg.setAttribute("height", height);

    const pegRadius = pegDiameter / 2;
    let pegCountX = width / (pegDiameter + (pegDiameter * pegSpacing)) - 1;
    let pegCountY = height / (pegDiameter + (pegDiameter * pegSpacing));
    let offsetX = pegRadius;


    for (let y = 0; y < pegCountY; y++) {
        offsetX = -offsetX;
        pegCountX = y % 2 == 0 ? pegCountX + 1 : pegCountX - 1;

        for (let x = 0; x < pegCountX; x++) {
            const peg = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            peg.setAttribute("fill", "#181818");
            peg.setAttribute("stroke", "#eee");
            peg.setAttribute("stroke-width", "3px");
            /*
            Math for getting X and Y:
                (pegRadius * x) gets the initial X coord for the circle
                (x * (pegSPacing * pegRadius)) gets the spacing between the pegs
                + pegRadius moves it a little over so it's not clipping
                + offsetX is what makes the pegs positioned in an alternating pattern
            */

            peg.setAttribute("cx", `${parseInt((pegDiameter * x) + (x * (pegSpacing * pegDiameter)) + pegDiameter + offsetX)}px`);
            peg.setAttribute("cy", `${parseInt((pegDiameter * y) + (y * (pegSpacing * pegDiameter)) + pegDiameter)}px`);
            peg.setAttribute("r", pegRadius);

            svg.appendChild(peg);
        }
    }

    document.body.append(svg);
}
