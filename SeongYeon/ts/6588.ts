const solution = (input: number[]) => {
  const eratos: (boolean | undefined)[] = [];
  const maxInput: number = Math.max(...input);
  let result: string = '';

  for (let i = 2; i * i <= maxInput; i++) {
    if (!eratos[i]) {
      for (let j = 2; i * j <= maxInput; j++) {
        eratos[i * j] = true;
      }
    }
  }

  input.forEach((n) => {
    if (n !== 0) {
      for (let i = 3; i <= n; i++) {
        if (!eratos[i] && !eratos[n - i]) {
          result += `${n} = ${i} + ${n - i}\n`;
          break;
        }
      }
    }
  });

  console.log(result);
};

const input = require('fs')
  .readFileSync('test/input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((a: string) => +a);
solution(input);
