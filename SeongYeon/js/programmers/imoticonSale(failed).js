function solution(users, emoticons) {
  let answer = [0, 0];
  let sale = [10, 20, 30, 40];
  let minSale = 40;

  users.forEach(([percent, price]) => {
    if (percent < minSale) minSale = percent;
  });
  sale = sale.filter((percent) => percent >= minSale);

  const caseList = permutation(sale, emoticons.length);
  caseList.forEach((cases) => {
    let tempAnswer = [0, 0];
    users.forEach((user) => {
      let price = 0;
      cases.forEach((percent, idx) => {
        if (user[0] <= percent) {
          price += (emoticons[idx] * (100 - percent)) / 100;
        }
      });
      if (price >= user[1]) tempAnswer[0]++;
      else tempAnswer[1] += price;
    });
    if (tempAnswer[0] >= answer[0] && tempAnswer[1] >= answer[1])
      answer = [...tempAnswer];
  });

  return answer;
}

const permutation = (arr, selectNum) => {
  const result = [];
  if (selectNum === 1) return arr.map((v) => [v]);

  arr.forEach((v, idx, arr) => {
    const fixed = v;
    const restArr = arr;
    const permutationArr = permutation(restArr, selectNum - 1);
    const combineFix = permutationArr.map((v) => [fixed, ...v]);
    result.push(...combineFix);
  });

  return result;
};
