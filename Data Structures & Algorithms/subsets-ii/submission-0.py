class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res, sol = [], []
        nums.sort()

        def backtrack(start):
            res.append(sol[:])
            
            for i in range(start, len(nums)):

                if i > start and nums[i] == nums[i-1]:
                    continue
            
                sol.append(nums[i])
                backtrack(i+1)
                sol.pop()
        
        backtrack(0)
        return res