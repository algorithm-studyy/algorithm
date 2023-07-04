function trap(height: number[]): number {
  let answer = 0;

  let start = 0;
  while (height[start] === 0) {
    start++;
  }

  let peak = height[start];
  let maybeHole = 0;
  let idx = start + 1;

  while (idx <= height.length && start < height.length) {
    if (idx === height.length) {
      if (maybeHole !== 0) {
        start += 1;
        idx = start + 1;
        peak = height[start];
        maybeHole = 0;
        continue;
      } else {
        break;
      }
    }

    if (height[idx] < peak) {
      maybeHole += peak - height[idx];
      idx++;
    } else {
      answer += maybeHole;
      maybeHole = 0;
      start = idx;
      peak = height[start];
      idx = start + 1;
    }
  }

  return answer;
}
