class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        area = 0
        stack = []

        for i in range(len(heights)):
            if not stack:
                stack.append([i, heights[i]])
            else:
                if heights[i] >= stack[-1][1]:
                    stack.append([i, heights[i]]) 
                else:
                    while stack and heights[i] < stack[-1][1]:
                        idx, ht = stack.pop()
                        if stack:
                            width = i - stack[-1][0] - 1
                        else:
                            width = i
                        area = width * ht
                        max_area = max(area, max_area)
                    stack.append([i, heights[i]])
        
        while stack:
            idx, ht = stack.pop()
            if stack:
                width = len(heights) - stack[-1][0] - 1
            else:
                width = len(heights)
            area = width * ht
            max_area = max(area, max_area)
        
        return max_area
                        