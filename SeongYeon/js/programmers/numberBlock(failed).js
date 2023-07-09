function solution(begin, end) {
  const answer = [];

  for (let i = begin; i <= end; i++) {
    if (i === 1) answer.push(0);
    else {
      for (let j = 2; j <= i; j++) {
        if (i % j === 0) {
          answer.push(i / j);
          break;
        }
      }
    }
  }

  return answer;
}
