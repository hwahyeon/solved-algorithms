const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').toString().split(' ');

const x = parseInt(input[0]);
const k = parseInt(input[1]);

if (k*7 <= x){
    console.log(k*7000)
} else if (k*3.5 <= x){
    console.log(k*3500)
} else if (k * 1.75 <= x) {
    console.log(k*1750)
} else {
    console.log(0)
}
