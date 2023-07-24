// Runtime: 69ms(Beats 54.00%)
// Memory: 43.98mb(Beats 82.71%)

function isValid(s: string): boolean {
  const leftBracket = ['(', '{', '['];
  const rightBracket = [')', '}', ']'];
  const stack = [];

  for (const bracket of s) {
    if (leftBracket.includes(bracket)) stack.push(bracket);
    else {
      const idx = rightBracket.indexOf(bracket);
      const peak = stack[stack.length - 1];

      if (!peak || peak !== leftBracket[idx]) return false;
      stack.pop();
    }
  }

  if (stack.length) return false;

  return true;
}
