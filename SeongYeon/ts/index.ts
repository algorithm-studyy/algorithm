const solution = (input: number[]) => {
  const [m, n] = input;
  const eratos: (boolean | undefined)[] = [];
  let result: string = '';
  for (let i = 2; i * i <= n!; i++) {
    if (!eratos[i]) {
      for (let j = 2; i * j <= n!; j++) {
        eratos[i * j] = true;
      }
    }
  }
  for (let i = m!; i <= n!; i++) {
    if (i > 1 && !eratos[i]) result += `${i}\n`;
  }
  console.log(result);
};

const input = require('fs')
  .readFileSync('test/input.txt')
  .toString()
  .trim()
  .split(' ')
  .map((a: string) => +a);
solution(input);
