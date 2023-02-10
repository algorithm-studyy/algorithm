// input
const input: number[] = require('fs')
  .readFileSync('test/input.txt')
  .toString()
  .trim()
  .split(' ')
  .map((a: string) => +a);

// variable
let result = '';
const [n, m] = input;
const nums: number[] = new Array(m);

// solution
const dfs = (depth: number) => {
  if (depth === m) {
    result += nums.join(' ') + '\n';
    return;
  }
  for (let i = 0; i < n!; i++) {
    nums[depth] = i + 1;
    dfs(depth + 1);
  }
};

dfs(0);

// output
console.log(result);
