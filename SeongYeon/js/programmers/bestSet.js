function solution(n, s) {
  if (n > s) return [-1];

  const devide = Math.floor(s / n);
  const answer = new Array(n).fill(devide);
  let rest = s % n;

  for (let i = n - rest; i < n; i++) answer[i] += 1;

  return answer;
}
