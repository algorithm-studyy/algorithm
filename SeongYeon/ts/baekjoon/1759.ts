// input
const input = require('fs')
  .readFileSync('test/input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
let result: string = '';
const [n, m]: number[] = input[0].split(' ').map((a: string) => +a);
const wordList: string[] = input[1].split(' ').sort();
const vowels: string[] = ['a', 'e', 'i', 'o', 'u'];
const tempList: string[] = [];

// solution
const dfs = (depth: number, start: number, numOfVowel: number) => {
  if (depth === n) {
    if (numOfVowel > 0 && numOfVowel <= n! - 2)
      result += tempList.join('') + '\n';
    return;
  }
  for (let i = start; i < m!; i++) {
    tempList[depth] = wordList[i]!;
    if (vowels.includes(wordList[i]!)) dfs(depth + 1, i + 1, numOfVowel + 1);
    else dfs(depth + 1, i + 1, numOfVowel);
  }
};

dfs(0, 0, 0);

// output
console.log(result);
