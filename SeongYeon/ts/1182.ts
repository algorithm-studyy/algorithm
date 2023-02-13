// input
const input: string[] = require('fs')
  .readFileSync('test/input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
const [n, s] = input[0]!.split(' ').map((a: string) => +a);
const nums: number[] = input[1]!.split(' ').map((a: string) => +a);
let result: number = 0;

// solution
for (let i = 1; i < 1 << n!; i++) {
  let sum: number = 0;
  for (let j = 0; j < n!; j++) {
    if (i & (1 << j)) sum += nums[j]!;
  }

  if (sum === s) result++;
}

// output
console.log(result);
