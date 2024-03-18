const input = require('fs').readFileSync('input.txt').toString().trim().split("\r\n");

let A = input[0];
let B = input[1];

console.log(A * B[2]);
console.log(A * B[1]);
console.log(A * B[0]);
console.log(A * Number(B));