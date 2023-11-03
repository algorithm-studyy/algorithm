function solution(n, stations, w) {
  const coverage = w * 2 + 1;
  let distance = 0;
  let answer = 0;

  stations.push(n + w + 1);
  for (let i = 0; i < stations.length; i++) {
    if (i === 0) distance = stations[i] - w - 1;
    else distance = stations[i] - stations[i - 1] - coverage;

    if (distance > 0) {
      const quotient = Math.floor(distance / coverage);
      const remainder = distance % coverage;

      answer += quotient + (remainder && 1);
    }
  }

  return answer;
}
