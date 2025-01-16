document.querySelector("#add-box-button").addEventListener("click", createBox);
document.querySelector("#add-item-button").addEventListener("click", addItem);

function createBox() {
    const boxes = document.querySelectorAll(".box").length;
    const box = document.createElement("div");
    box.className = "box";
    box.id = boxes;
    box.addEventListener("click", e=>e.target.classList.add("selected"));
    document.querySelector("main").appendChild(box);
    box.classList.add("selected");
}
// Make it deselect the old box after new box is selected
function addItem() {
    const item = document.createElement("div");

}