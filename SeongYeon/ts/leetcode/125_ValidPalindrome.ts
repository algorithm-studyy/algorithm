function isPalindrome(s: string): boolean {
  const alphaNumeric = s.replace(/[^A-Za-z0-9]/gi, '');
  const lowerCase = alphaNumeric.toLowerCase();

  return lowerCase === lowerCase.split('').reverse().join('') ? true : false;
}
