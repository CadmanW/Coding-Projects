// Import http and file system
const http = require("node:http");
const fs = require("node:fs");

// Get the index.html file contents
let html;
fs.readFile("login/index.html", "utf8", (e, contents) => {
    e ? console.error(e) : html = contents;
});


// Set the host and port for the server
const hostname = "127.0.0.1";
const port = 3000;

// Set up server
const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader("Content-Type", "text/html");
    res.end(html);
});

// Tell server to listen to set port and hostname
server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});