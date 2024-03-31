// Update the X and Y values of the mouse
const mouse = {
    x: 0,
    y: 0
}
document.addEventListener("mousemove", (event) => {
    mouse.x = event.clientX;
    mouse.y = event.clientY;
});


// Function for creating the particle
function createParticle () {
    // Get a random value for color and size
    const color = Math.floor(Math.random() * 10000);
    const size = (Math.random() * 10) ** 1.2;

    // Create and style the particle
    const particle = document.createElement("div");
    particle.style.position = "absolute";
    particle.style.backgroundColor = `#${color}`;
    particle.style.width = `${size}px`;
    particle.style.height = `${size}px`;
    particle.style.borderRadius = `${size / 2}px`;
    particle.style.left = `${mouse.x}px`;
    particle.style.top = `${mouse.y}px`;

    // Set the duration, x, y, and seed of the particle
    particle.ariaLabel = `0 0 0 ${Math.random()}`;

    // Add the particle to the webpage
    document.body.appendChild(particle);
}


// Animate the particles
let oldDuration = 0;

// This function runs when last call has endedand all affected elements are drawn on the page
function tick(newDuration) {
    // Get Delta
    const delta = (newDuration - oldDuration) * 0.01;
    oldDuration = newDuration;

    // 20% chance to create the particle
    if (Math.random() * 10 >= 8) createParticle();

    //Iterate through all particles
    for (particle of document.querySelectorAll("div")) {

        // Parse the aria-label for particle specifics
        let ariaLabel = particle.ariaLabel.split(" ");
        const duration = Number(ariaLabel[0]);
        let x = Number(ariaLabel[1]);
        let y = Number(ariaLabel[2]);
        const seed = Number(ariaLabel[3]) - 0.5;

        // If the particle is alive for more than 3s, delete it
        if (duration > 3000) {
            particle.remove();
        }
        
        // Change the particle's position
        x += delta * 0.1;
        let direction = Math.floor(seed - 0.5);
        let amplitude = (seed + 0.5) * direction;
        y = (amplitude * (x ** 2));
        

        particle.style.transform = `translate(${x}px, ${y}px)`;

        // Update aria-label
        ariaLabel = `${duration + delta} ${x} ${y} ${seed}`;
        particle.ariaLabel = ariaLabel;
    }

    requestAnimationFrame(tick);
}

requestAnimationFrame(tick);