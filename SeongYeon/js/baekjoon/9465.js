// input
const fs = require('fs');
const inputFile =
  process.platform === 'linux' ? '/dev/stdin' : 'test/input.txt';
const input = fs.readFileSync(inputFile).toString().split('\n');

let t = Number(input[0]);

// solution
let result = '';
let row = 1;

while (t--) {
  const stickers = [];
  const length = input[row++];
  stickers[0] = input[row++].split(' ').map(Number);
  stickers[1] = input[row++].split(' ').map(Number);

  const dp = [
    [0, stickers[0][0]],
    [0, stickers[1][0]],
  ];
  for (let i = 2; i <= length; i++) {
    dp[0][i] = Math.max(dp[1][i - 1], dp[1][i - 2]) + stickers[0][i - 1];
    dp[1][i] = Math.max(dp[0][i - 1], dp[0][i - 2]) + stickers[1][i - 1];
  }

  result += `${Math.max(dp[0][length], dp[1][length])}\n`;
}

// output
console.log(result);
