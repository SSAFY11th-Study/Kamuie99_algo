const input = require('fs').readFileSync('input.txt').toString().split(' ');

let t = Number(input[0]);
let m = Number(input[1]);

if (m >= 45) {
  console.log(t, m - 45)
} else if (t >= 1) {
  console.log(t - 1, m + 15)  /* +60 -45 는 +15 */
} else {
  console.log(23, m + 15)
};
