// input
const input = require('fs')
  .readFileSync('test/input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
let result: number = 10000;
const n: number = Number(input.shift());
const mergedInput: number[][] = Array.from(Array(n), () => new Array(n));
const isStartMember: boolean[] = new Array(n).fill(false);

for (let i = 0; i < n; i++) {
  for (let j = i; j < n; j++) {
    mergedInput[i][j] =
      Number(input[i].split(' ')[j]) + Number(input[j].split(' ')[i]);
  }
}

// solution
const dfs = (start: number, depth: number) => {
  if (depth === n / 2) {
    const startMember = [];
    const linkMember = [];
    for (const i in isStartMember) {
      if (isStartMember[i]) startMember.push(i);
      else linkMember.push(i);
    }
    const isPair: boolean[] = new Array(n / 2).fill(false);
    const startSum: number = dfs2(startMember, isPair, 0, 0);
    const linkSum: number = dfs2(linkMember, isPair, 0, 0);
    const subtract = Math.abs(startSum - linkSum);
    if (subtract < result) result = subtract;
    return;
  }
  for (let i = start; i < n; i++) {
    if (isStartMember[i]) continue;
    isStartMember[i] = true;
    dfs(i + 1, depth + 1);
    isStartMember[i] = false;
  }
};

const dfs2 = (
  list: number[],
  isPair: boolean[],
  start: number,
  depth: number
): number => {
  if (depth === 2) {
    const pairIdx = [];
    for (const i in isPair) {
      if (isPair[i]) pairIdx.push(i);
    }
    return 0;
  }
  for (let i = start; i < n / 2; i++) {
    if (isPair[i]) continue;
    isPair[i] = true;
    dfs2(list, isPair, i + 1, depth + 1);
    isPair[i] = false;
  }
};

dfs(0, 0);

// output
console.log(result);
