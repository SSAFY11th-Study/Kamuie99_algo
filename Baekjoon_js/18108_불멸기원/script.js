const input = require('fs').readFileSync('input.txt').toString().split(' ');

let Bul_year = Number(input[0]);

let year = Bul_year - 543;

console.log(year);