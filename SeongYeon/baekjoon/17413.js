// input
const input = require('fs').readFileSync('test/input.txt').toString();

// solution
let result = '';
let reversing = true;
const stack = [];
for (let char of input) {
  if (char === '<') {
    if (reversing) while (stack.length) result += stack.pop();
    reversing = false;
    result += char;
  } else if (char === '>') {
    reversing = true;
    result += char;
  } else if (char === ' ' && reversing) {
    while (stack.length) result += stack.pop();
    result += char;
  } else if (!reversing) {
    result += char;
  } else {
    stack.push(char);
  }
}
while (stack.length) result += stack.pop();

// output
console.log(result.replace(/\n/g, ''));
