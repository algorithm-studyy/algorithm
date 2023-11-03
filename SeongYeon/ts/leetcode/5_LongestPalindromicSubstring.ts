// Runtime 68.36% Memory 66.35%

function longestPalindrome(s: string): string {
  if (s.length === 1) return s;
  let res = s[0];

  for (let i = 0; i < s.length - 1; i++) {
    const even = getPalindrome(i, i + 1, s);
    const odd = getPalindrome(i, i + 2, s);

    if (even.length > res.length) res = even;
    if (odd.length > res.length) res = odd;
  }

  return res;
}

function getPalindrome(left: number, right: number, s: string): string {
  while (left >= 0 && right <= s.length && s[left] === s[right]) {
    left--;
    right++;
  }
  return s.substring(left + 1, right);
}
