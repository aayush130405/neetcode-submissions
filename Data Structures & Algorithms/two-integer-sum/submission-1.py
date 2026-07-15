class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            if target - v not in seen:
                seen[v] = i
            else:
                return [seen[target-v], i]