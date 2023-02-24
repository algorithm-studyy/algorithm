// input
const input: string[] = require('fs')
  .readFileSync('test/input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
let max: string = '';
let min: string = '9999999999';
let condition: boolean = true;
const k: number = Number(input[0]);
const brackets: string[] = input[1]!.split(' ');
const nums: number[] = new Array(k + 1);
const visitedNums: boolean[] = new Array(10).fill(false);

// solution
const dfs = (depth: number) => {
  if (depth === k + 1) {
    const result: string = nums.join('');
    if (result > max) max = result;
    if (result < min) min = result;
    return;
  }
  for (let i = 0; i < 10; i++) {
    if (visitedNums[i]) continue;
    nums[depth] = i;
    visitedNums[i] = true;
    if (depth === 0) {
      condition = true;
    } else {
      if (brackets[depth - 1] === '>') condition = nums[depth - 1]! > i;
      else condition = nums[depth - 1]! < i;
    }
    if (condition) dfs(depth + 1);
    visitedNums[i] = false;
  }
};

dfs(0);

// output
console.log(max + '\n' + min);
