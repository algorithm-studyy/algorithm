// input
const input: string = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input.txt')
  .toString()
  .trim();

// variable
const n: number = Number(input);
let dp: number[] = [0, 0];

// solution
for (let i = 2; i <= n; i++) {
  dp[i] = dp[i - 1]! + 1;
  if (i % 2 === 0) dp[i] = Math.min(dp[i]!, dp[i / 2]! + 1);
  if (i % 3 === 0) dp[i] = Math.min(dp[i]!, dp[i / 3]! + 1);
}

// output
console.log(dp[n]);
