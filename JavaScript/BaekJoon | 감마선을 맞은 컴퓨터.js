const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

for (let i = 0; i < 15; i++) {
  let board = input[i].trim().split(' ');

  if (board.includes('w')) {
    console.log('chunbae');
    break;
  } else if (board.includes('b')) {
    console.log('nabi');
    break;
  } else if (board.includes('g')) {
    console.log('yeongcheol');
    break;
  }
}
