const fs = require('fs');
const inputFile = '/dev/stdin';
const input = fs
  .readFileSync(inputFile)
  .toString()
  .split('\n')
  .map(function (a) {
    return +a;
  });
const n = input[0];

const stack = [];
let number = 1;
let result = [];

for (let i = 1; i <= n; i++) {
  while (number <= input[i]) {
    stack.push(number);
    result.push('+');
    number++;
  }
  if (stack.pop() !== input[i]) {
    result = ['NO'];
    break;
  }
  result.push('-');
}

console.log(result.join('\n'));
