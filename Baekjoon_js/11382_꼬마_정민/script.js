const input = require('fs').readFileSync('/dev/stdin').toString().split(' ');

let A = Number(input[0]);
let B = Number(input[1]);
let C = Number(input[2]);

console.log(A + B + C);
