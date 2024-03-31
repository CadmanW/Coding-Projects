const mouse = {
    x: 0,
    y: 0
}

document.addEventListener("mousemove", (event) => {
    mouse.x = event.clientX;
    mouse.y = event.clientY;
});









function createParticle () {

    const seed = Math.random();

    const color = Math.floor(seed * 1000000);
    const size = (seed * 10) ** 1.2;

    const particle = document.createElement("div");
    ariaLabel = 0;

    particle.style.position = "absolute";
    particle.style.backgroundColor = `#${color}`;
    particle.style.width = `${size}px`;
    particle.style.height = `${size}px`;
    particle.style.borderRadius = `${size / 2}px`;
    particle.style.left = `${mouse.x}px`;
    particle.style.top = `${mouse.y}px`;
    particle.ariaLabel = `0 0 0 ${Math.random()}`;

    document.body.appendChild(particle);
}









let oldDuration = 0;

function tick(newDuration) { 
    const delta = newDuration - oldDuration;
    oldDuration = newDuration;

    if (Math.random() * 10 >= 8) createParticle();

    const particles = document.querySelectorAll("div");

    if (particles) {
        for (particle of particles) {
            let ariaLabel = particle.ariaLabel.split(" ");
            const duration = Number(ariaLabel[0]);
            let x = Number(ariaLabel[1]);
            let y = Number(ariaLabel[2]);
            const seed = Number(ariaLabel[3]) - 0.5;

            if (duration > 3000) {
                particle.remove();
                continue;
            }
            
            y = seed * (x ** 2);
            x += seed * 10;

            particle.style.transform = `translate(${x}px, ${y}px)`;

            ariaLabel = `${duration + delta} ${x} ${y} ${seed}`;
            particle.ariaLabel = ariaLabel;
        }
    }

    requestAnimationFrame(tick);
}

tick(0);