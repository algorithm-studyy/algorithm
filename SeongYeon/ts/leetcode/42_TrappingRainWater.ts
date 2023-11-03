function trap(height: number[]): number {
  let answer = 0;
  let left = 0;
  let right = height.length - 1;
  let leftMax = 0,
    rightMax = 0;

  while (left < right) {
    if (height[left] <= height[right]) {
      leftMax = Math.max(leftMax, height[left]);
      answer += leftMax - height[left];
      left++;
    } else {
      rightMax = Math.max(rightMax, height[right]);
      answer += rightMax - height[right];
      right--;
    }
  }

  return answer;
}
