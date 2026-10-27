class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(i):
            n = len(nums)
            if i == n:
                res.append(sol[:])
                return 
            
            #do not choose
            backtrack(i+1)

            #choose
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res