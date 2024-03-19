// 백준 제출할 때는 신기하게도 \r을 빼야 한다 왤깡
const input = require('fs').readFileSync('input.txt', 'utf-8').trim().split('\r\n');

let values = input[0].split(' ');
let hour = Number(values[0]);
let min = Number(values[1]);
let oven = Number(input[1]);

min = min + oven;

// 분을 시간과 분으로 분해
let hoursToAdd = Math.floor(min / 60);
let minutesLeft = min % 60;

// 새로운 시간 계산
hour += hoursToAdd;
hour %= 24; // 24를 넘어가면 다시 0부터 시작

console.log(hour, minutesLeft);