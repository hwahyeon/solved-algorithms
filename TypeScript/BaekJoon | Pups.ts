const fs = require('fs');
let p = fs.readFileSync('/dev/stdin').toString().split("\n");

for (let i = 1; i <= p[0]; i++){
    const arr = p[i].split(' ').map(Number)
    let res = arr.reduce( (a:number, b:number) => a * b )
    console.log(`$${res.toFixed(2)}`)
}
