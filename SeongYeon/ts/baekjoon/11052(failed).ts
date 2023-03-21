// input
const input: string = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
const n: number = Number(input[0]);
const p: number[] = [0, ...input[1]!.split(' ').map((a: string) => +a)];
const dp: number[] = [0, p[1]!];

// solution
for (let i = 2; i <= n; i++) {
  if (dp[i - 1]! + dp[1]! < p[i]!) dp[i] = p[i]!;
  else dp[i] = dp[i - 1]! + dp[1]!;
}

// output
console.log(dp[n]);
