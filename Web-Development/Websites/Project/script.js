const shapesBox = document.getElementById('shapes-box');


window.addEventListener('dragstart', (e) => {
    e.dataTransfer.setData("application/my-app", e.target.id);
    e.dataTransfer.effectAllowed = "move";
});


shapesBox.addEventListener('dragover', (e) => {
    e.preventDefault();
    e.dataTransfer.dropEffect = "move";
});


shapesBox.addEventListener('drop', (e) => {
    e.preventDefault();

    const shape = e.dataTransfer.getData("application/my-app");
    const shapeArea = e.target;

    if (shape === shapeArea.attributes.name.value) {
        document.getElementById(shape).remove();

        alert("correct!");
    } else {
        alert("wrong :(");
    }
    
});