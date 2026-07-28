class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temp)

        for i in range(len(temp)):
            if not stack:
                stack.append([i, temp[i]])
            else:
                while stack and temp[i] > stack[-1][1]:
                    result[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
                stack.append([i, temp[i]])
        return result