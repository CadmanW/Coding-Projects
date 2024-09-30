const fetchBtn = document.querySelector("button");
const ul = document.querySelector("ul");

fetchBtn.addEventListener('click', (e) => {
    fetch("https://pokeapi.co/api/v2/pokemon/?offset=100&limit=100")
    .then((re) => re.json())
    .then((json) => {
        json.results.forEach((poke) => {
            const el = document.createElement("li");
            el.textContent = poke.name;
            ul.appendChild(el);
        });
    });
});