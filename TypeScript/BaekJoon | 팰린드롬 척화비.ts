var fs = require("fs")
var input = fs.readFileSync("/dev/stdin").toString()
console.log("a".repeat(Number(input)))
