class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()
        res, path = [], []

        def backtrack(start, total):
            if total == target:
                res.append(path[:])
                return
            
            if total > target:
                return 

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])
                backtrack(i+1, total + nums[i])
                path. pop()

        backtrack(0, 0)
        return res