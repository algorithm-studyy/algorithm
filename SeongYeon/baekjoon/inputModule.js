const fs = require('fs');
const inputFile = 'test/input.txt';
// const inputFile = '/dev/stdin';

// const input = fs.readFileSync(inputFile).toString();
// const input = fs.readFileSync(inputFile).toString().split(' ');
// const input = fs.readFileSync(inputFile).toString().split('\n');
const input = fs
  .readFileSync(inputFile)
  .toString()
  .split('\n')
  .map(function (a) {
    return +a;
  });

module.exports = input;
