const modal = document.querySelector("dialog");

// Event listeners for addBox and addItem
document.querySelector("#add-box-button").addEventListener("click", createBox);
document.querySelector("#add-item-button").addEventListener("click", addItem);

// Creates a box
function createBox() {
    const boxNum = document.querySelectorAll(".box").length;

    const boxEl = document.createElement("div");
    boxEl.className = "box";
    boxEl.id = boxNum;
    boxEl.addEventListener("click", e=>selectBox(document.getElementById(e.target.ariaLabel))); // Whenever a box is clicked, the target returned as "e" is the superior child of said box, so I gave them all aria labels that let them "belong" to a box. Box is then selected using the aria label of it's child.

    const titleEl = document.createElement("h1");
    titleEl.classList.add("title");
    titleEl.ariaLabel = boxNum;
    titleEl.textContent = `Box #${boxNum}`;
    
    const itemListEl = document.createElement("ul");
    itemListEl.classList.add("item-list");
    itemListEl.ariaLabel = boxNum;

    boxEl.appendChild(titleEl);
    boxEl.appendChild(itemListEl);
    document.querySelector("main").appendChild(boxEl);
    selectBox(boxEl);
}

// Deselects old box and selects new box clicked
function selectBox(box) {
    try { document.querySelectorAll(".selected")[0].classList.remove("selected") }
    catch (e) { console.error("Can't unselect box if there is no box selected") }

    box.classList.add("selected");
}

// Createa an item that belongs to the selected box
function addItem() {
    const item = document.createElement("li");
    
    modal.showModal();
}