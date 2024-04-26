const sensor = new Gyroscope({frequency: 60});
sensor.oldX = 0;
sensor.oldY = 0;
let absX = 0;
let absY = 0;

sensor.onreading = () => {
    document.querySelector("#template").style.transform = `
        rotateX(${sensor.y}rad)
        rotateY(${sensor.x}rad)
    `;
}

sensor.start();