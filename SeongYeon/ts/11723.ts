// input
const input: string[] = require('fs')
  .readFileSync('test/input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
let s: number = 0;

// solution
input.forEach((command, idx) => {
  if (idx !== 0) {
    const split: string[] = command.split(' ');
    const operator: string = split[0]!;
    const x: number = Number(split[1]);

    if (operator === 'add') {
      s |= 1 << (x - 1);
    } else if (operator === 'remove') {
      s &= ~(1 << (x - 1));
    } else if (operator === 'check') {
      if (s & (1 << (x - 1))) console.log(1);
      else console.log(0);
    } else if (operator === 'toggle') {
      s ^= 1 << (x - 1);
    } else if (operator === 'all') {
      s = (1 << 20) - 1;
    } else if (operator === 'empty') {
      s = 0;
    }
  }
});
