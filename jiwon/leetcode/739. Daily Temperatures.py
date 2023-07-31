# stack에 아무것도 없으면 삽입
# while(stack[-1] < t) stack.pop() count += 1 [1...] 
# stack.append(t)
# while len(answer) < len(temps) stack.append(0)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer, stack = [0] * len(temperatures), [] 
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                value, idx = stack.pop()
                answer[idx] = i - idx
            stack.append([t, i])

        return answer
