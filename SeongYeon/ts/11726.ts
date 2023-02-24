// input
const input: string = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input.txt')
  .toString()
  .trim();

// variable
const n: number = Number(input);
let dp: number[] = [0, 1, 2];

// solution
for (let i = 3; i <= n; i++) {
  dp[i] = (dp[i - 1]! + dp[i - 2]!) % 10007;
}

// output
console.log(dp[n]);
