// Runtime: 68ms(Beats 59.24%)
// Memory: 44.89mb(Beats 43.19%)

function isValid(s: string): boolean {
  const stack = [];
  const bracketPair = {
    ')': '(',
    '}': '{',
    ']': '[',
  };

  for (const bracket of s) {
    if (bracket in bracketPair) {
      if (!stack.length || stack.pop() !== bracketPair[bracket]) return false;
    } else stack.push(bracket);
  }

  return !stack.length;
}
