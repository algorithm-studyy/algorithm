// input
const input: string = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
const n: number = Number(input[0]);
const nums: number[] = input[1]!.split(' ').map((a: string) => +a);
const dp: number[] = new Array(n).fill(1);

// solution
for (let i = 1; i < n; i++) {
  for (let j = 0; j < i; j++) {
    if (nums[j]! < nums[i]!) {
      dp[i] = Math.max(dp[i]!, dp[j]! + 1);
    }
  }
}

// output
console.log(Math.max(...dp));
