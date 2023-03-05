// input
const input: string = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input.txt')
  .toString()
  .trim();

// variable
const n: number = Number(input);
const dp: number[] = [0, 3, 7];

// solution
for (let i = 2; i < n; i++) {
  dp[i + 1] = (dp[i - 1]! * 3 + (dp[i]! - dp[i - 1]!) * 2) % 9901;
}

// output
console.log(dp[n]);
