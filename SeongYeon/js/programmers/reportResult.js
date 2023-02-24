function solution(id_list, report, k) {
  let answer = new Array(id_list.length).fill(0);
  const count = {};
  id_list.forEach((id) => {
    count[id] = 0;
  });

  const reportSet = new Set(report);
  const reportList = [...reportSet].map((str) => str.split(' '));

  reportList.forEach((tuple) => {
    count[tuple[1]]++;
  });

  const blackList = Object.keys(count).filter((key) => count[key] >= k);

  reportList.forEach((tuple) => {
    if (blackList.includes(tuple[1])) answer[id_list.indexOf(tuple[0])]++;
  });

  return answer;
}
