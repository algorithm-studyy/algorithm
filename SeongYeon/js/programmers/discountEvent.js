function solution(want, number, discount) {
  const wantNumber = {};
  let res = 0;

  want.forEach((item, idx) => {
    wantNumber[item] = number[idx];
  });

  for (let i = 0; i <= discount.length - 10; i++) {
    const wantNumberCopy = { ...wantNumber };

    for (let j = 0; j < 10; j++) {
      const saleItem = discount[i + j];
      if (wantNumberCopy[saleItem] !== undefined) wantNumberCopy[saleItem]--;
    }

    res++;
    for (const key in wantNumberCopy) {
      if (wantNumberCopy[key] !== 0) {
        res--;
        break;
      }
    }
  }

  return res;
}
