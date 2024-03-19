/* 왜인지는 모르겠으나, 이 문제는 백준에 제출할 때, readFileSync(0)으로 해야 됨...*/
const input = require('fs').readFileSync('input.txt').toString().split('\n');

const x = Number(input[0]);
const y = Number(input[1]);

if (x > 0 && y > 0) {
  console.log(1)
} else if (x < 0 && y > 0) {
  console.log(2)
} else if (x < 0 && y < 0) {
  console.log(3)
} else if (x > 0 && y < 0) {
  console.log(4)
};




