class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[right]:
                return min(res, nums[left])
            elif nums[left] > nums[mid]:
                res = min(res, nums[mid])
                right = mid - 1
            else:
                left = mid + 1