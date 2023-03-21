// input
const input: string = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input.txt')
  .toString()
  .trim();

// variable
const n: number = Number(input);
const dp: bigint[] = [0, 1, 1].map((num: number) => BigInt(num));

// solution
for (let i = 3; i <= n; i++) {
  dp[i] = dp[i - 1]! + dp[i - 2]!;
}

// output
console.log(dp[n]!.toString());
