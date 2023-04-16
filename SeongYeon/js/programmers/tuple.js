function solution(s) {
  const nums = s.replace(/[{}]/g, '').split(',');
  const numCount = {};
  const res = [];

  nums.forEach((num) => {
    numCount[num] = (numCount[num] | 0) + 1;
  });

  for (const [key, value] of Object.entries(numCount)) {
    res[value - 1] = Number(key);
  }

  return res.reverse();
}
