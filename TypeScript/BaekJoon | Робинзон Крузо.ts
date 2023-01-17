const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString();
let n: number = Number(input)
console.log('V'.repeat(Number(n/5))+'I'.repeat(n%5))
