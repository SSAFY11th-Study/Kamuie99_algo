const input = require('fs').readFileSync('input.txt', 'utf-8').trim().split('\r\n');

for (let i = 0; i < input.length; i++) {
  let numbers = input[i].split(' ')
  const A = Number(numbers[0])
  const B = Number(numbers[1])
  if (A != 0) {
    console.log(A + B)
  }
};