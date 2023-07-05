function trap(height: number[]): number {
  let answer = 0;
  let peak = 0;
  let nextPeak = 0;
  let isReverse = false;

  for (let i = 0; i < height.length; i++) {
    if (i >= nextPeak) {
      peak = nextPeak;
      let max = 0;
      let maybePeak = 0;
      for (let j = i + 1; j < height.length; j++) {
        if (height[j] >= height[peak]) {
          nextPeak = j;
          isReverse = false;
          break;
        }
        if (height[j] > max) {
          maybePeak = j;
          max = height[j];
        }
      }
      if (peak === nextPeak) {
        nextPeak = maybePeak;
        isReverse = true;
      }
    } else {
      if (isReverse) answer += height[nextPeak] - height[i];
      else answer += height[peak] - height[i];
    }
  }

  return answer;
}
