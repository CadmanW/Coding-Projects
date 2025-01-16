// Event listeners for addBox and addItem
document.querySelector("#add-box-button").addEventListener("click", createBox);
document.querySelector("#add-item-button").addEventListener("click", addItem);

// Deselects old box and selects new box clicked
function selectBox(box) {
    try { document.querySelectorAll(".selected")[0].classList.remove("selected") }
    catch (e) { console.error("Can't unselect box if there is no box selected") }

    box.classList.add("selected");
}

// Creates a box
function createBox() {
    const boxes = document.querySelectorAll(".box").length;
    const box = document.createElement("div");
    box.className = "box";
    box.id = boxes;
    box.addEventListener("click", e=>selectBox(e.target));
    document.querySelector("main").appendChild(box);
    selectBox(box);
}

// Createa an item that belongs to the selected box
async function addItem() {
    const item = document.createElement("div");
    
}

function openModal() {
    
}