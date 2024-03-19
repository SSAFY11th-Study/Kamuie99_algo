const fs = require('fs');
const input = fs.readFileSync('input.txt', 'utf-8').trim().split(' ');

const N = Number(input[0])

console.log((1 + N) * N / 2)