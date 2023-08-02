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
  let answer = 0;

  const dfs = (rowIdx, depth, score) => {
    if (depth >= length) {
      answer = Math.max(answer, score);
      return;
    }

    if (rowIdx === 0) {
      dfs(1, depth + 1, score + stickers[rowIdx][depth]);
      dfs(1, depth + 2, score + stickers[rowIdx][depth]);
    } else {
      dfs(0, depth + 1, score + stickers[rowIdx][depth]);
      dfs(0, depth + 2, score + stickers[rowIdx][depth]);
    }
  };

  for (let i = 0; i <= 1; i++) {
    dfs(i, 0, 0);
  }

  result += `${answer}\n`;
}

// output
console.log(result);
