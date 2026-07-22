class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        area = 0
        max_area = 0

        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i-1])

        for i in reversed(range(len(height))):
            if i == len(height) - 1:
                continue
            else:
                right_max[i] = max(right_max[i+1], height[i+1])

        for i in range(1, len(height) - 1):
            area = min(left_max[i], right_max[i]) - height[i]

            if area > 0:
                max_area += area
            else:
                continue

        return max_area