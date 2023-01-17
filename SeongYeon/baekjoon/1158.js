// input
const fs = require('fs');
const inputFile = 'test/input.txt';
const [n, k] = fs.readFileSync(inputFile).toString().split(' ');

// solution
let result = [];
let people = [];
let count = 0;
for (let i = 1; i <= n; i++) people.push(i);

while (people.length !== 0) {
  people.push(people.shift());
  if (++count % k === 0) result.push(people.pop());
}

// output
console.log(`<${result.join(', ')}>`);
