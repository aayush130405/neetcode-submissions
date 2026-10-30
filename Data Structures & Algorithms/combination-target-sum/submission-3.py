class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start):
            if sum(path) > target:
                return 

            if sum(path) == target:
                res.append(path[:])
                return 
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i)
                path.pop()
        
        backtrack(0)
        return res

            