const input = require('fs').readFileSync('input.txt').toString().split(' ');

let A = Number(input[0]);
let B = Number(input[1]);

console.log(A / B);
console.log(input);