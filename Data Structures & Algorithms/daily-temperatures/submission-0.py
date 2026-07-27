class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack = []
        result = [0] * len(t)

        for i in range(len(t)):
            if not stack:
                stack.append([i, t[i]])
            else:
                while stack and t[i] > stack[-1][1]:
                    result[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
                stack.append([i, t[i]])
        
        return result
