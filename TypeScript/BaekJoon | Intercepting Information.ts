const fs = require('fs');
let arr = fs.readFileSync('/dev/stdin').toString().split(' ');

if (arr.find(e => e == '9') == undefined) {
    console.log('S')
} else {
    console.log('F')
}
