// input
const input = require('fs')
  .readFileSync('test/input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
let result: number = 0;
const n: number = Number(input.shift());
const tList: number[] = input.map((str: string) => Number(str.split(' ')[0]));
const pList: number[] = input.map((str: string) => Number(str.split(' ')[1]));

// solution
const dfs = (idx: number, sum: number) => {
  if (idx >= n) {
    if (sum > result) result = sum;
    return;
  }
  dfs(idx + tList[idx]!, sum + pList[idx]!);
  dfs(idx + 1, sum + pList[idx]!);
};

dfs(0, 0);

// output
console.log(result);
