const fs = require('fs');
let arr = fs.readFileSync('/dev/stdin').toString().split('');
let full = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];

for (let i = 0; i < arr.length; i++) { 
  if (arr.includes(full[i])) { 
    full.splice(i, 1); 
    i--; 
  }
}

console.log(full[0]);
