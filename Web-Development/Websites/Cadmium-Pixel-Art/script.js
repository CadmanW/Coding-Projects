function updateCanvasSize(x, y) {

    if (x % 2) {} else {
        x++, y++
    }

    canvas.innerHTML = null;

    canvas.style.gridTemplateRows = `repeat(${y}, 1fr)`;
    canvas.style.gridTemplateColumns = `repeat(${x}, 1fr)`;

    const size = pixelSize(x, y);

    for (let i = 0; i < (x * y); i++) {
        if (i % 2) {
            createPixel("#eee", size);
        } else {
            createPixel("#aaa", size);
        }
    }
}

function createPixel(bgColor, size) {
    const pixel = document.createElement("div");

    pixel.style.backgroundColor = bgColor;
    pixel.style.width = `${size}px`
    pixel.style.height = `${size}px`

    canvas.appendChild(pixel);
}

function pixelSize(x, y) {
    x = canvasContainer.clientWidth / x;
    y = canvasContainer.clientHeight / y;

    return Math.min(x * 0.9, y * 0.9);
}






// get elements from DOM
const pixelsX = document.querySelector("#pixels-input-x");
const pixelsY = document.querySelector("#pixels-input-y");
const pixelsApplyButton = document.querySelector(".pixels-submit-button");
const canvasContainer = document.querySelector(".canvas-container");
const canvas = document.querySelector(".canvas");
const color = document.querySelector("#colorInput");


// change the size of the canvas
pixelsApplyButton.addEventListener("click", ()=>{
    updateCanvasSize(pixelsX.value, pixelsY.value);
});

let mouseX;
let mouseY

// Drawing on the canvas
canvas.addEventListener("mousemove", (event)=>{

    if (canvas.matches(":hover") && canvas.matches(":active")) {
        mouseX = event.clientX;
        mouseY =event.clientY;

        const pixel = document.elementFromPoint(mouseX, mouseY);
        pixel.style.backgroundColor = color.value;
    }

});