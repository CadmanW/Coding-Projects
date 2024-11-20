const gameContainerEl = document.querySelector("#game-container"); // game-container is 1000 x 1000 px
const dropBallButtonEl = document.querySelector("#drop-ball-button");
const plinkoBoard = initPlinkoBoard(1000, 600, 25, 1.5, gameContainerEl, 20, 200);





let ball;

dropBallButtonEl.addEventListener("click", e => {
    ball = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    ball.setAttribute("cx", "500");
    ball.setAttribute("cy", "50");
    ball.setAttribute("r", "20");
    ball.setAttribute("id", "ball");

    ball.oldX = 500;
    ball.oldY = 50;

    gameContainerEl.appendChild(ball);

    requestAnimationFrame(ballProccess);
});


let oldTime = 0;
let vector = new Vector(0.0, 0.0, 0.0);

function ballProccess(time) {
    const delta = time - oldTime;
    oldTime = time;

    // Gravity
    console.log(new Vector((vector.x > 0.0 ? vector.x * 0.9 : vector.x * 1.1), (vector.y * 1.1), 1.0).times(delta));



    // Update ball position with vector
    ball.setAttribute("cx", vector.x * vector.a);
    ball.setAttribute("cy", vector.y * vector.a);

    
    requestAnimationFrame(ballProccess);
}







function initPlinkoBoard(width, height, pegDiameter, pegSpacing, parentElement, svgX, svgY) {
    // Create the SVG for the plinko board
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg")
    svg.setAttribute("viewbox", `0 0 ${width} ${height}`);
    svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
    svg.setAttribute("width", width);
    svg.setAttribute("height", height);
    svg.setAttribute("x", svgX);
    svg.setAttribute("y", svgY);

    const pegRadius = pegDiameter / 2;
    // pegCount represents how many pegs that have a diameter and spacing bewtween them fit in a given length
    let pegCountX = width / (pegDiameter + (pegDiameter * pegSpacing)) - 1; // subtract one for formatting and prettiness
    let pegCountY = height / (pegDiameter + (pegDiameter * pegSpacing));
    let offsetX = pegRadius; // peg rows are moved left and right by the offset every other row 


    // Create the pegs
    for (let y = 0; y < pegCountY; y++) {
        offsetX = -offsetX;
        pegCountX = y % 2 == 0 ? pegCountX + 1 : pegCountX - 1; // add a peg on every other row for formatting and prettiness

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

    parentElement.append(svg);

    return svg;
}
