// input
const input: string[] = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
const n: number = Number(input.shift());
const tList: number[] = [
  0,
  ...input.map((str: string) => Number(str.split(' ')[0])),
];
const pList: number[] = [
  0,
  ...input.map((str: string) => Number(str.split(' ')[1])),
];
const dp: number[] = new Array(n + 1).fill(0);

// solution
for (let i = 1; i <= n; i++) {
  dp[i] = dp[i - 1]!;
  for (let j = i; j >= 1; j--) {
    if (tList[j]! + j - 1 === i)
      dp[i] = Math.max(dp[i]!, pList[j]! + dp[j - 1]!);
  }
}

// output
console.log(dp[n]);
