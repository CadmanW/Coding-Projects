const sqrSize = 50;


window.addEventListener("load", ()=>{
    Object.keys(letters).forEach(letter => {

        bitmap = letters[letter]

        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", bitmap[0].length * sqrSize)
        svg.setAttribute("height", bitmap.length * sqrSize)
        


        for (let y in bitmap) {
            for (let x in bitmap[y]) {
                const sqr = document.createElementNS("http://www.w3.org/2000/svg", "rect");

                sqr.setAttribute("x", sqrSize * x);
                sqr.setAttribute("y", sqrSize * y);

                sqr.setAttribute("width", sqrSize)
                sqr.setAttribute("height", sqrSize)

                console.log(x)
                if (bitmap[y][x] === 1) {
                    sqr.setAttribute("fill", "#0000ff")
                } else {
                    sqr.setAttribute("fill", "#ffffff")
                }

                sqr.setAttribute("stroke", "#000000")

                svg.appendChild(sqr)
            }
        }
        document.body.appendChild(svg);
    });
});