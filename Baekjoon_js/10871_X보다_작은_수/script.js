const input = require('fs').readFileSync('input.txt', 'utf-8').trim().split('\r\n');

const N_X = input[0].split(' ');
const N = Number(N_X[0]);
const X = Number(N_X[1]);

const numbers = input[1].split(' ');

let result = [];

for (let i = 0; i < N; i++) {
  let check = Number(numbers[i])
  if (check < X) {
    result.push(check)
  }
}

console.log(result.join(' '));