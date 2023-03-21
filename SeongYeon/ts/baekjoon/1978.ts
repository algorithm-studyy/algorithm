const solution = (input: number[]) => {
  let result = 0;
  input.forEach((num) => {
    if (num !== 1) {
      let isPrime = true;
      for (let i = 2; i * i <= num; i++) {
        if (num % i === 0) {
          isPrime = false;
          break;
        }
      }
      if (isPrime) result++;
    }
  });
  console.log(result);
};

const input = require('fs')
  .readFileSync('test/input.txt')
  .toString()
  .trim()
  .split('\n');
const inputList = input[1].split(' ').map((a: string) => +a);
solution(inputList);
