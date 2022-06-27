const fs = require('fs');
const n = fs.readFileSync("/dev/stdin").toString().trim();

const res = [0, 1]; 
    for (let i = 2; i <= n; i++) { 
    	const a = res[i - 1]; 
        const b = res[i - 2]; 
        res.push(a + b); 
    } 
console.log(res[n]);
