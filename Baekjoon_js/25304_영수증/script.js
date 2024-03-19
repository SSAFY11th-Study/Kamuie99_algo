const input = require('fs').readFileSync('input.txt', 'utf-8').trim().split('\r\n');

const total_price = Number(input[0]);
const produt_count = Number(input[1]);
let calculate = 0;

for (let i = 1; i <= produt_count; i++) {
  let price_count = input[i + 1].split(' ')
  let price = Number(price_count[0])
  let count = Number(price_count[1])
  calculate += price * count
};

if (total_price == calculate) {
  console.log('Yes')
} else {
  console.log('No')
};