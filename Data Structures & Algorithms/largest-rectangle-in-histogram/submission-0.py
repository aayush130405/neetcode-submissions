class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        area = 0

        for i in range(len(heights)):
            if not stack:
                stack.append([i, heights[i]])
            else:
                while stack and stack[-1][1] > heights[i]:
                    index, ht = stack.pop()
                    if stack:
                        width = i - stack[-1][0] - 1
                    else:
                        width = i
                    area = ht * width
                    max_area = max(area, max_area)
                stack.append([i, heights[i]])

        while stack:
            idx, ht = stack.pop()
            if stack:
                width = len(heights) - stack[-1][0] - 1
            else:
                width = len(heights)
            
            area = ht * width
            max_area = max(area, max_area)

        return max_area