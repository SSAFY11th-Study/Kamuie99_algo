const input = require('fs').readFileSync('input.txt', 'utf-8').trim();

let N = Number(input);

N /= 4;

console.log('long '.repeat(N) + 'int');