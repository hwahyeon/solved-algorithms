const fs = require('fs');
let p = fs.readFileSync('/dev/stdin').toString().split("\n");

for (let i = 1; i <= p[0]; i++){
    const arr = p[i].split('')
    let res = [arr[0]]
    let comparison = arr[0]
    
    for (let j = 1; j < arr.length; j++){
        if (arr[j] !== comparison){
            res.push(arr[j])
            comparison = arr[j]
        }
    }
    console.log(res.join(''))
}
