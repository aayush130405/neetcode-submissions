class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        area = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            if heights[left] > heights[right]:
                area = heights[right] * (right - left)
                max_area = max(max_area, area)

                right -= 1
            else:
                area = heights[left] * (right - left)
                max_area = max(max_area, area)

                left += 1

        return max_area