function solution(s) {
  let opened = 0;

  for (let bracket of s) {
    opened += bracket === '(' ? 1 : -1;
    if (opened < 0) return false;
  }

  if (opened !== 0) return false;
  return true;
}
