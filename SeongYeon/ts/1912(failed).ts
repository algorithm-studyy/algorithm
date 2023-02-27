// input
const input: string = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
const MIN_NUMBER = -1000;
const n: number = Number(input[0]);
const nums: number[] = input[1]!.split(' ').map((a: string) => +a);
const dp: number[] = input[1]!.split(' ').map((a: string) => +a);

// solution
for (let i = 1; i < n; i++) {
  let temp: number = nums[i]!;
  for (let j = i - 1; j >= 0; j--) {
    temp += nums[j]!;
    dp[i] = Math.max(temp, dp[i]!);
  }
}

// output
console.log(Math.max(...dp));
