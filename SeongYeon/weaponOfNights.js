function solution(number, limit, power) {
  let answer = 0;
  for (let i = 1; i <= number; i++) {
    answer += getDivisorCount(i, limit, power);
  }
  return answer;
}

const getDivisorCount = (num, limit, power) => {
  let cnt = 0;
  for (let i = 1; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      cnt++;
      if (num / i !== i) cnt++;
    }
  }

  return cnt <= limit ? cnt : power;
};
