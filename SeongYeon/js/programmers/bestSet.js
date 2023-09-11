function solution(n, s) {
  if (n > s) return [-1];

  const devide = Math.floor(s / n);
  const answer = new Array(n).fill(devide);
  let rest = s % n;
  let idx = n - 1;

  while (rest !== 0) {
    answer[idx] += 1;
    rest--;
    idx--;
  }

  return answer;
}
