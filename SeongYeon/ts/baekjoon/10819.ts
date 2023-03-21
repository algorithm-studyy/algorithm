// input
const input: string[] = require('fs')
  .readFileSync('test/input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
const n: number = Number(input[0]);
const nums: number[] = input[1]!.split(' ').map((a: string) => +a);
const visited: boolean[] = new Array(n).fill(false);
let max: number = 0;

// solution
const dfs = (depth: number, prevNum: number, sum: number) => {
  if (depth === n) {
    if (max < sum) max = sum;
    return;
  }
  for (let i = 0; i < n; i++) {
    if (visited[i]) continue;
    visited[i] = true;
    if (depth === 0) dfs(depth + 1, nums[i]!, sum);
    else dfs(depth + 1, nums[i]!, sum + Math.abs(prevNum - nums[i]!));
    visited[i] = false;
  }
};

dfs(0, 0, 0);

// output
console.log(max);
