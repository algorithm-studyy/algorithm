// input
const input: number[] = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split(' ')
  .map((a: string) => +a);

// variable
let result = '';
const [n, m] = input;
const nums: number[] = new Array(m);

// solution
const dfs = (depth: number, start: number) => {
  if (depth === m) {
    result += nums.join(' ') + '\n';
    return;
  }
  for (let i = start; i < n!; i++) {
    nums[depth] = i + 1;
    dfs(depth + 1, i + 1);
  }
};

dfs(0, 0);

// output
console.log(result);
