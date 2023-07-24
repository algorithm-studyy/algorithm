// Runtime: 63ms(Beats 79.89%)
// Memory: 44.02mb(Beats 80.22%)

function isValid(s: string): boolean {
  const leftBracket = ['(', '{', '['];
  const rightBracket = [')', '}', ']'];
  const stack = [];

  for (const bracket of s) {
    if (leftBracket.includes(bracket)) stack.push(bracket);
    else {
      const idx = rightBracket.indexOf(bracket);
      if (stack.pop() !== leftBracket[idx]) return false;
    }
  }

  return !stack.length;
}
