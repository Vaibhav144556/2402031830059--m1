const express = require("express");

const app = express();

app.get("/", (req, res) => {
    res.send("I love India ❤️");
    res.send("hello world");
    res.send("my name is vaibhav gupta");
});

app.listen(3000, () => {
    console.log("Server running on http://localhost:3000");
});