const fs = require('fs');
const inputFile = 'test/input.txt';
const input = fs.readFileSync(inputFile).toString().split('\n');

const stack = [];
let top = -1;
input.forEach((value) => {
  console.log(value);
});
