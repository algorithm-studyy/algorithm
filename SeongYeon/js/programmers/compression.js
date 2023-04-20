function solution(msg) {
  const dictionary = [...' ABCDEFGHIJKLMNOPQRSTUVWXYZ'];
  const res = [];

  let start = 0;
  while (start < msg.length) {
    let find = '';
    for (let i = dictionary.length - 1; i > 0; i--) {
      if (msg.substr(start, dictionary[i].length) === dictionary[i]) {
        res.push(i);
        find = dictionary[i];
        start += find.length;
        break;
      }
    }
    if (start < msg.length) dictionary.push(find + msg[start]);
  }

  return res;
}
