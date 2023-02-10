// input
const input: string[] = require('fs')
  .readFileSync('test/input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
let result = '';
const [n, m] = input[0]!.split(' ').map((a: string) => +a);
const inputList = input[1]!
  .split(' ')
  .map((a: string) => +a)
  .sort();
const nums: number[] = new Array(m);
const visited: boolean[] = new Array(m);

// solution
const dfs = (depth: number) => {
  if (depth === m) {
    result += nums.join(' ') + '\n';
    return;
  }
  for (let i = 0; i < n!; i++) {
    if (visited[i]) continue;
    visited[i] = true;
    nums[depth] = inputList[i]!;
    dfs(depth + 1);
    visited[i] = false;
  }
};

dfs(0);

// output
console.log(result);
