class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[right]:
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] < nums[mid]:
                if nums[left] < target < nums[mid]:
                    right = mid 
                else:
                    left = mid + 1 
            else:
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid
        return -1 