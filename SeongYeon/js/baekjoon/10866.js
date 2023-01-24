// input
const fs = require('fs');
const inputFile = 'test/input2.txt';
const input = fs.readFileSync(inputFile).toString().split('\n');

// solution
let result = '';
const deque = [];
for (let i = 1; i < input.length; i++) {
  const command = input[i];
  if (command === 'pop_front') result += `${deque.shift() || -1}\n`;
  else if (command === 'pop_back') result += `${deque.pop() || -1}\n`;
  else if (command === 'size') result += `${deque.length}\n`;
  else if (command === 'empty') result += `${deque.length ? 0 : 1}\n`;
  else if (command === 'front') result += `${deque[0] || -1}\n`;
  else if (command === 'back') result += `${deque[deque.length - 1] || -1}\n`;
  else {
    const [direction, x] = command.split(' ');
    if (direction === 'push_front') deque.unshift(x);
    else deque.push(x);
  }
}

// output
console.log(result);
