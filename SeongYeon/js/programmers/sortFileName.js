function solution(files) {
  const reArrange = [];

  files.forEach((file) => {
    const number = file.match(/\d+/g)[0];
    const numberIdx = file.indexOf(number);
    const head = file.substring(0, numberIdx);
    const tail = file.substring(numberIdx + number.length);

    reArrange.push({ head, number, tail });
  });

  reArrange.sort((a, b) => {
    const smallA = a.head.toLowerCase();
    const smallB = b.head.toLowerCase();

    if (smallA < smallB) return -1;
    else if (smallA > smallB) return 1;
    else {
      if (+a.number < +b.number) return -1;
      else if (+a.number > +b.number) return 1;
      else return 0;
    }
  });

  return reArrange.map((obj) => obj.head + obj.number + obj.tail);
}
