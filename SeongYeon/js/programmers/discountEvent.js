function solution(want, number, discount) {
  let res = 0;

  for (let i = 0; i < discount.length - 9; i++) {
    const discountTenDays = discount.slice(i, i + 10);
    res++;
    for (const idx in want) {
      const count = discountTenDays.filter((item) => item === want[idx]).length;
      if (count !== number[idx]) {
        res--;
        break;
      }
    }
  }

  return res;
}
