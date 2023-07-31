class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        stack.append(temperatures[0])
        for i in range(1, len(temperatures)):
            if temperatures[i] < stack[-1]:
                stack.append(temperatures[i])
                print(answer)
            else:
                answer.append(i - (len(stack)-1))

        return answer