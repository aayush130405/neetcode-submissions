class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        nums.sort()

        def backtrack(i):
            res.append(sol[:])
            for x in range(i, len(nums)):
                if x > i and nums[x] == nums[x-1]:
                    continue
                
                sol.append(nums[x])
                backtrack(x+1)
                sol.pop()
        
        backtrack(0)
        return res