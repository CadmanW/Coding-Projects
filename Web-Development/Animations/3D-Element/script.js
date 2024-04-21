document.addEventListener("mousemove", (mouse) => {

    const x = mouse.clientX;
    const y = mouse.clientY;

    const middleX = window.innerWidth / 2;
    const middleY = window.innerHeight / 2;

    const offsetX = x - middleX;
    const offsetY = y - middleY;

    const radX = offsetX / middleX;
    const radY = offsetY / middleY * -1;

    document.querySelector("pre").style.transform = `
                rotateX(${radY}rad)
                rotateY(${radX}rad)
            `;
});