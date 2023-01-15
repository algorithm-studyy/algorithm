// input
const input = require('./inputModule.js');
const n = input[0];

// solution
const stack = [];
let number = 1;
let result = '';

for (let i = 1; i <= n; i++) {
  while (number <= input[i]) {
    stack.push(number);
    result += '+\n';
    number++;
  }
  if (stack.pop() !== input[i]) {
    result = 'NO';
    break;
  }
  result += '-\n';
}

// output
console.log(result);
