// input
const input: string = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input.txt')
  .toString()
  .trim();

// variable
const [n, k] = input.split(' ').map((a: string) => +a);
const dp: number[][] = Array.from(Array(n! + 1), () => Array(k! + 1).fill(0));

// solution
for (let i = 1; i <= n!; i++) {
  dp[i]![1] = 1;
  dp[i]![2] = i + 1;
}

for (let j = 1; j <= k!; j++) {
  dp[1]![j] = j;
}

for (let i = 2; i <= n!; i++) {
  for (let j = 3; j <= k!; j++) {
    for (let m = i; m >= 1; m--) {
      dp[i]![j] += dp[m]![j - 1]!;
    }
  }
}

// output
console.log(dp[n!]![k!]);
