const input = require('fs').readFileSync('input.txt', 'utf-8').trim().split('\r\n');

const N = Number(input[0]);
let field = input[1].split(' ');
field = field.map(Number);

const max = Math.max(...field);
const min = Math.min(...field);

console.log(min, max);