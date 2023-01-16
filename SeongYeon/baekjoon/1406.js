// input
const fs = require('fs');
const inputFile = 'test/input2.txt';
const input = fs.readFileSync(inputFile).toString().split('\n');

// solution
const left = input[0].split('');
const right = [];

for (let i = 2; i < input.length; i++) {
  const command = input[i][0];
  if (command === 'L' && left.length !== 0) right.push(left.pop());
  else if (command === 'D' && right.length !== 0) left.push(right.pop());
  else if (command === 'B' && left.length !== 0) left.pop();
  else left.push(input[i][2]);
}

const result = left.join('') + right.reverse().join('');

// output
console.log(result);
