// input
const input: string[] = require('fs')
  .readFileSync('test/input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
let result = '';
let nums: number[] = [];
let k: number = 0;
let visited: boolean[] = [];

// solution
const dfs = (depth: number, start: number, str: string) => {
  if (depth === 6) {
    result += str + '\n';
    return;
  }

  for (let i = start; i < k; i++) {
    if (visited[i]) continue;
    visited[i] = true;
    dfs(depth + 1, i, str + nums[i] + ' ');
    visited[i] = false;
  }
};

input.forEach((element) => {
  if (element !== '0') {
    nums = element.split(' ').map((a) => +a);
    k = nums.shift()!;
    visited = [];
    dfs(0, 0, '');
    result += '\n';
  }
});

// output
console.log(result);
