// input
const fs = require('fs');
const inputFile = '/dev/stdin';
const input = fs.readFileSync(inputFile).toString().split('\n');

// solution
let result = '';
const queue = [];
for (let i = 1; i < input.length; i++) {
  const command = input[i];
  if (command === 'pop') result += `${queue.shift() || -1}\n`;
  else if (command === 'size') result += `${queue.length}\n`;
  else if (command === 'empty') result += `${queue.length ? 0 : 1}\n`;
  else if (command === 'front') result += `${queue[0] || -1}\n`;
  else if (command === 'back') result += `${queue[queue.length - 1] || -1}\n`;
  else queue.push(command.split(' ')[1]);
}

// output
console.log(result);
