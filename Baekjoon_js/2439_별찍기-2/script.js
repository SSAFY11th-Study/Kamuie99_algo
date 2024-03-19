const input = require('fs').readFileSync('input.txt', 'utf-8').trim();

const N = Number(input);

for (let i = 1; i <= N; i++) {
  console.log(' '.repeat(N - i) + '*'.repeat(i))
};

