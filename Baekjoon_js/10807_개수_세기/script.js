const input = require('fs').readFileSync('input.txt', 'utf-8').trim().split('\r\n');

const N = Number(input[0]);
const numbers = input[1].split(' ');
const find_number = input[2];

let count = 0;

for (let i = 0; i < N; i++) {
  if (numbers[i] == find_number) {
    count++;
  }
}

console.log(count);