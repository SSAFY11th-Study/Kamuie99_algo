const fs = require('fs');
const numbers = fs.readFileSync('input.txt', 'utf-8').trim().split(' ');

let A = Number(numbers[0]);
let B = Number(numbers[1]);
let C = Number(numbers[2]);

if (A == B && B == C) {
  console.log(10000 + A * 1000)
} else if (A == B || A == C) {
  console.log(1000 + A * 100)
} else if (B == C) {
  console.log(1000 + B * 100)
} else {
  let max_value = Math.max(A, B, C)
  console.log(max_value * 100)
};


