const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');

let [x, y] = input
console.log(x - y);
