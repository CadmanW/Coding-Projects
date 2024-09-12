const sqrSize = 50;

Object.keys(letters).forEach(letter=>{

    const svg = document.createElement("svg");
    svg.viewBox = "0 0 900 900";
    svg.xmlns = "http://www.w3.org/2000/svg";

    for (let y of letters[letter]) {
        for (let x of y) {
            
            svg.innerHTML += `<rect width="${sqrSize}" height="${sqrSize}" />`;

        }
    }


    document.body.append(svg);
});