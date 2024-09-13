const sqrSize = 15;

// Wait for the window to load
window.addEventListener("load", ()=>{
    // for every key entry in the bitmaps object
    Object.keys(bitmaps).forEach(key => {

        // get the bitmap itself
        const bitmap = bitmaps[key];

        // Make the SVG
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", bitmap[0].length * sqrSize);
        svg.setAttribute("height", bitmap.length * sqrSize);
        
        //* Draw the squares in the SVG
        // For every row in the bitmap
        for (let row in bitmap) {
            // For every entry in the row
            for (let x in bitmap[row]) {

                // Create the square
                const sqr = document.createElementNS("http://www.w3.org/2000/svg", "rect");
                sqr.setAttribute("x", sqrSize * x);
                sqr.setAttribute("y", sqrSize * row);
                sqr.setAttribute("width", sqrSize);
                sqr.setAttribute("height", sqrSize);
                sqr.setAttribute("stroke", "#000000");

                //* Figure out what color we fill the square with
                let fillColor = null;

                // Check the length of the rows
                switch (bitmaps[key][0].length) {
                    case (3):
                        fillColor = "#ffc000";
                        break;
                    case (4):
                        // Make it a different color if the bitmap is representing a number
                        if (Number.isInteger(parseInt(key))) {
                            fillColor = "#70ad47";
                        } else {
                            fillColor = "#5b9bd5"
                        }
                        break;
                    case (5):
                        fillColor = "#ed7d31";
                        break;
                }

                // If the current square of the bitmap holds 1, then fill the square
                if (bitmap[row][x] === 1) {
                    sqr.setAttribute("fill", fillColor);
                } else {
                    sqr.setAttribute("fill", "#ffffff");
                }

                // Add the square to the SVG
                svg.appendChild(sqr);
            }
        }
        // Add the SVG to the DOM
        document.body.appendChild(svg);
    });
});