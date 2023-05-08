function solution(numbers) {
  const res = numbers
    .sort((a, b) => (`${a}${b}` > `${b}${a}` ? -1 : 1))
    .join('');
  return Number(res) === 0 ? '0' : res;
}
