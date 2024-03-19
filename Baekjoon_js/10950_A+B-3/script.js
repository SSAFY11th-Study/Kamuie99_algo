const fs = require('fs');
const input = fs.readFileSync('input.txt', 'utf-8').trim().split('\r\n');
// vscode에서는 이렇게 사용하지만, 백준에서는 .split('\n');

let count = Number(input[0]);

for (let i = 1; i <= count; i++) {
  let numbers = input[i].split(' ')
  let result = Number(numbers[0]) + Number(numbers[1])
  console.log(result)
};