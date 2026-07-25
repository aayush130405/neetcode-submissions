class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_water = 0
        water = 0

        while left < right:
            if heights[left] < heights[right]:
                water = heights[left] * (right - left)
                max_water = max(water, max_water)

                left += 1
            else:
                water = heights[right] * (right - left)
                max_water = max(water, max_water)
        
                right -= 1
        return max_water