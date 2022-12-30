function solution(k, score) {
  const answer = [];
  const hallOfFame = new Array(k);
  let min = 0;
  for (const [day, eachScore] of Object.entries(score)) {
    if (day < k) {
      hallOfFame[day] = eachScore;
      min = Math.min(...hallOfFame.filter(Number.isInteger));
    } else if (min < eachScore) {
      const minIdx = hallOfFame.indexOf(min);
      hallOfFame[minIdx] = eachScore;
      min = Math.min(...hallOfFame);
    }
    answer.push(min);
  }
  return answer;
}
