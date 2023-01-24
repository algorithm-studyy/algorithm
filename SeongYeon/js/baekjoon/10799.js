// input
const input = require('fs').readFileSync('test/input2.txt').toString().trim();

// solution
let result = 0;
const stack = [];
for (let i = 0; i < input.length; i++) {
  if (input[i] === '(') stack.push(0);
  else {
    stack.pop();
    if (input[i - 1] === '(') result += stack.length;
    else result += 1;
  }
}

// output
console.log(result);
