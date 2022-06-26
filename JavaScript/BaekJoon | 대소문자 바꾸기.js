let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim();
let res = "";

for (let i = 0; i < input.length; i++) {
    if (input[i] === input[i].toUpperCase()) {
        res += input[i].toLowerCase()
    } else {
        res += input[i].toUpperCase()
    }
}

console.log(res);
