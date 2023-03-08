// input
const input: string[] = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
const dp: number[][] = input.map((item) => item.split(' ').map(Number));
const n: number = dp[0]![0]!;

// solution
for (let i = 2; i <= n; i++) {
  for (let j = 0; j < i; j++) {
    if (j === 0) dp[i]![j] += dp[i - 1]![j]!;
    else if (j === i - 1) dp[i]![j] += dp[i - 1]![j - 1]!;
    else {
      dp[i]![j] += Math.max(dp[i - 1]![j]!, dp[i - 1]![j - 1]!);
    }
  }
}

// output
console.log(Math.max(...dp[n]!));
