class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, sol = [], []

        def backtrack(start, total):
            if total == target:
                res.append(sol[:])
                return
            
            if total > target:
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                sol.append(nums[i])
                backtrack(i+1, nums[i] + total)
                sol.pop()
            
        backtrack(0, 0)
        return res