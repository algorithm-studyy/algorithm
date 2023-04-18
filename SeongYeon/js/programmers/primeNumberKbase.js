function solution(n, k) {
  const str = n.toString(k);
  const list = str.replace(/0+/g, '0').split('0').map(Number);
  let res = 0;

  list.forEach((num) => {
    if (num < 2) return;
    for (let i = 2; i * i <= num; i++) {
      if (num % i === 0) return;
    }
    res++;
  });

  return res;
}
