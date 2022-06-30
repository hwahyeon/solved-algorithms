const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').toString().split(' ');

const a = parseInt(input[0]);
const b = parseInt(input[1]);

if (a * 0.01 * (100-b) >= 100){
    console.log(0)
} else {
    console.log(1)
}
