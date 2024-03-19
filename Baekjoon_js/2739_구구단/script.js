const input = require('fs').readFileSync('input.txt', 'utf-8').trim().split(' ');

let N = Number(input[0]);

for (let i = 1; i <= 9; i++) {
  console.log(`${N} * ${i} = ${N * i}`)
};