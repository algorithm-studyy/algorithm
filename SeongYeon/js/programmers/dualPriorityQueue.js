function solution(operations) {
  const heap = [];

  operations.forEach((operation) => {
    const [opt1, opt2] = operation.split(' ');
    if (opt1 === 'I') {
      heap.push(Number(opt2));
      heap.sort((a, b) => b - a);
    } else {
      if (opt2 === '1') {
        heap.shift();
      } else {
        heap.pop();
      }
    }
  });

  return heap.length === 0 ? [0, 0] : [heap[0], heap[heap.length - 1]];
}
