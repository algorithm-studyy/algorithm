function solution(n, t, m, p) {
  let number = 0;
  let str = '';
  let res = '';

  while (str.length <= m * t) {
    str += number.toString(n).toUpperCase();
    number++;
  }

  while (res.length < t) {
    res += str[p - 1];
    p += m;
  }

  return res;
}
