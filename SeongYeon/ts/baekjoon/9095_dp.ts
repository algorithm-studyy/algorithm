// input
const input: number[] = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((a: string) => +a);

// variable
let result: string = '';
let dp: number[] = [0, 1, 2, 4];

// solution
for (let i = 4; i <= 11; i++) {
  dp[i] = dp[i - 1]! + dp[i - 2]! + dp[i - 3]!;
}

input.forEach((n, idx) => {
  if (idx !== 0) result += dp[n] + '\n';
});

// output
console.log(result);
