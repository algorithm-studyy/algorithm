function solution(X, Y) {
  let answer = '';
  for (number of X) {
    if (Y.includes(number)) {
      answer += number;
      Y = Y.replace(number, '');
    }
  }

  if (!answer) return '-1';
  if (Number(answer) === 0) return '0';
  return answer
    .split('')
    .sort((a, b) => b - a)
    .join('');
}
