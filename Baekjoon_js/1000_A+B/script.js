const input = require('fs').readFileSync('/dev/stdin').toString().split(' ');

let num_1 = Number(input[0]);
let num_2 = Number(input[1]);

console.log(num_1 + num_2);
