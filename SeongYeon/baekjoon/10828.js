const fs = require('fs');
const inputFile = 'input.txt';
const inputList = fs.readFileSync(inputFile).toString().split('\n');

const stack = [];
let top = -1;
inputList.forEach((input) => {
  console.log(input);
});
