// input
const input: string[] = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
const n: number = Number(input[0]);
const inputList: number[] = input[1]!.split(' ').map(Number);
const dp: number[] = [inputList[0]!];

// solution
for (let i = 1; i < n; i++) {
  dp[i] = dp[i - 1]! < 0 ? inputList[i]! : dp[i - 1]! + inputList[i]!;
}

let removeIdx = -1;
let subtract = Number.MAX_SAFE_INTEGER;
for (let i = 1; i < n - 1; i++) {
  if (dp[i]! - dp[i - 1]! < subtract) {
    subtract = dp[i]! - dp[i - 1]!;
    removeIdx = i;
  }
}

if (inputList[removeIdx]! < 0) {
  dp[removeIdx] = dp[removeIdx - 1]!;

  for (let i = removeIdx + 1; i < n; i++) {
    dp[i] = dp[i - 1]! < 0 ? inputList[i]! : dp[i - 1]! + inputList[i]!;
  }
}

// output
console.log(Math.max(...dp));
