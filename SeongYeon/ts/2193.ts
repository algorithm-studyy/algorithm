// input
const input: string = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input.txt')
  .toString()
  .trim();

// variable
const n: number = Number(input);
const dp: bigint[][] = [
  [BigInt(0), BigInt(0)],
  [BigInt(0), BigInt(1)],
];

// solution
for (let i = 2; i <= n; i++) {
  dp[i] = [BigInt(0), BigInt(0)];
  if (dp[i - 1]![0]) {
    dp[i]![0] += dp[i - 1]![0]!;
    dp[i]![1] += dp[i - 1]![0]!;
  }
  if (dp[i - 1]![1]) dp[i]![0] += dp[i - 1]![1]!;
}

// output
const result = dp[n]![0]! + dp[n]![1]!;
console.log(result.toString());
