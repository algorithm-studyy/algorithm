let count: number = 0;

const solution = (input: number[]) => {
  let result: string = '';
  for (let i = 1; i < input.length; i++) {
    count = 0;
    dfs(0, input[i]!);
    result += count + '\n';
  }
  console.log(result);
};

const dfs = (sum: number, n: number) => {
  for (let i = 1; i <= 3; i++) {
    if (sum >= n) {
      if (sum === n) count++;
      return;
    }
    dfs(sum + i, n);
  }
};

const input = require('fs')
  .readFileSync('test/input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((a: string) => +a);
solution(input);
