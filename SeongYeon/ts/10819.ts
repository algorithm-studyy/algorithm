// input
const input: string[] = require('fs')
  .readFileSync('test/input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
const n: number = Number(input[0]);
const nums: number[] = input[1]!.split(' ').map((a: string) => +a);
const resultNums: number[] = new Array(n);
const visited: boolean[] = new Array(n).fill(false);
let max: number = 0;

// solution
const dfs = (depth: number) => {
  if (depth === n) {
    let result: number = 0;
    for (let i = 1; i < n; i++) {
      result += Math.abs(resultNums[i - 1]! - resultNums[i]!);
    }
    if (result > max) max = result;
    return;
  }
  for (let i = 0; i < n; i++) {
    if (visited[i]) continue;

    resultNums[depth] = nums[i]!;
    visited[i] = true;
    dfs(depth + 1);
    visited[i] = false;
  }
};

dfs(0);

// output
console.log(max);
