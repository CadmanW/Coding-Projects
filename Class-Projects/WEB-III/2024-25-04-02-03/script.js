const cowBitmap = [
    [0, 0, 2, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 2, 1, 3, 3, 3, 2, 0, 0],
    [3, 3, 1, 1, 3, 3, 1, 3, 3, 3],
    [0, 1, 1, 1, 3, 1, 1, 1, 3, 0],
    [0, 0, 1, 5, 1, 1, 5, 1, 0, 0],
    [0, 4, 4, 4, 4, 4, 4, 4, 4, 0],
    [0, 4, 4, 3, 4, 4, 3, 4, 4, 0],
    [0, 0, 4, 4, 4, 4, 4, 4, 0, 0]
];
/*
0: empty
1: white
2: hornColor
3: darkColor
4: lightColor
5: eyeColor
*/

function drawCow(color) {
    // constant colors
    const eyeColor = "#362F2F";
    const hornColor = "#C6841F";
    const white = "#eeeeee";

    // variable colors
    let lightColor;
    let darkColor;
    switch (color) {
        case "blue":
            lightColor = "#196B90";
            darkColor = "#1784A5";
            break;
        case "green":
            lightColor = "#417628";
            darkColor = "#3F7F10";
            break;
        case "purple":
            lightColor = "#633A78";
            darkColor = "#625A8E";
            break;
        case "pink":
            lightColor = "#C2585C";
            darkColor = "#BD6B6F";
            break;
        case "orange":
            lightColor = "#C46125";
            darkColor = "#BC6718";
            break;
        case "brown":
            lightColor = "#7B4430";
            darkColor = "#934332";
            break;
        case "red":
            lightColor = "#A22526";
            darkColor = "#AB2D37";
            break;
    }
    const colors = {
        0: "none",
        1: white,
        2: hornColor,
        3: darkColor,
        4: lightColor,
        5: eyeColor
    }
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
    svg.setAttribute("viewbox", "0 0 200 160");
    document.body.appendChild(svg);


    // draw the cow
    for (let y = 0; y < 8; y++) {
        for (let x = 0; x < 10; x++) {
            const sqrColor = colors[cowBitmap[y][x]];

            const sqr = document.createElementNS("http://www.w3.org/2000/svg", "rect");
            sqr.setAttribute("width", "20");
            sqr.setAttribute("height", "20");
            sqr.setAttribute("x", x * 20);
            sqr.setAttribute("y", y * 20);
            sqr.setAttribute("fill", sqrColor);

            svg.appendChild(sqr);
        }
    }
}


drawCow("blue");
drawCow("green");
drawCow("purple");
drawCow("pink");
drawCow("orange");
drawCow("brown");
drawCow("red");