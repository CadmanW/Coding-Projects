const circle = {el: document.querySelector("#circle"), x: 0, y: 0}
const mouse = {x: 0, y: 0, preX: 0, preY: 0, deltaX: 0, deltaY: 0, angle: 0}

document.addEventListener("mousemove", (e) => {
    mouse.x = e.x;
    mouse.y = e.y;
});

// the lower the number, the more the circle will lage behind the mouse
const speed = 0.17;

const tick = () => {
    // Make the circle follow the mouse, but lag behind it by a factor of the speed variable by
    // adding the difference between the circle's and the mouse's position to the position of the circle
    circle.x += (mouse.x - circle.x) * speed;
    circle.y += (mouse.y - circle.y) * speed;
    let transform = ` translate(${circle.x}px, ${circle.y}px)`;

    // Calculate the distance between old and new mouse coordinates
    mouse.deltaX = mouse.x - mouse.preX;
    mouse.deltaY = mouse.y - mouse.preY;

    // Calculate the angle using tan then rotate the circle
    mouse.angle = Math.atan2(mouse.deltaY, mouse.deltaX) * 180 / Math.PI;
    transform += ` rotate(${mouse.angle}deg)`;

    // Update old mouse values after they're used
    mouse.preX = mouse.x;
    mouse.preY = mouse.y;
    
    // Calculate mouse velocity using the pythagorean theorum, and cap the value to 150
    const mouseVelocity = Math.min(Math.sqrt((mouse.deltaX)**2 + (mouse.deltaY)**2), 150);

    // Divide the velocity by the velocity's cap to get it near a number used for scale()
    const scaleValue = (mouseVelocity / 150);

    // Scale the circle by adding/subtracting 1 to the scaleValue so that the X and Y scale oppositely
    transform +=` scale(${1 + scaleValue}, ${1 - scaleValue}`;

    // Update the location of circle
    circle.el.style.transform = transform;

    // Call this function again
    window.requestAnimationFrame(tick);
}

tick();