class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            if target - value not in seen:
                seen[value] = index
            else:
                return [seen[target-value], index]