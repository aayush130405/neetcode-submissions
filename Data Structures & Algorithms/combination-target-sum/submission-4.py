class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def bt(i, cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return 
            
            if i == len(nums) or cur_sum > target:
                return 
            
            # choose not to select that particular number and then recurse
            bt(i+1, cur_sum)

            # choose the current number and recurse 
            sol.append(nums[i])
            bt(i, cur_sum + nums[i])
            sol.pop()

        bt(0, 0)
        return res