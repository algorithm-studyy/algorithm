// input
const input: string[] = require('fs')
  .readFileSync('test/input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
let min: number = Number.MAX_SAFE_INTEGER;
let startIdx: number = 0;
let cost: number = 0;
const n: number = Number(input.shift());
const inputArr: number[][] = Array.from(Array(n), () => new Array(n));
const visited: boolean[] = new Array(n);

for (let i = 0; i < n; i++) {
  const row = input[i]!.split(' ');
  for (let j = 0; j < n; j++) {
    inputArr[i]![j] = Number(row[j]);
  }
}

// solution
const dfs = (depth: number, prevIdx: number, sum: number) => {
  if (depth === n - 1) {
    if (inputArr[prevIdx]![startIdx] !== 0) {
      min = Math.min(min, sum + inputArr[prevIdx]![startIdx]!);
    }
    return;
  }

  for (let i = 0; i < n; i++) {
    cost = inputArr[prevIdx]![i]!;
    if (visited[i] || cost === 0 || sum + cost > min) continue;

    visited[i] = true;
    dfs(depth + 1, i, sum + cost);
    visited[i] = false;
  }
};

for (let i = 0; i < n; i++) {
  startIdx = i;
  visited[i] = true;
  dfs(0, startIdx, 0);
  visited[i] = false;
}

// output
console.log(min);
