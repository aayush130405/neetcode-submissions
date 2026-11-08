class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, curr = [], []
        n = len(nums)

        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(curr[:])
                return
            
            if cur_sum > target or i == n:
                return
            
            backtrack(i + 1, cur_sum)

            curr.append(nums[i])
            backtrack(i, nums[i] + cur_sum)
            curr.pop()
        
        backtrack(0, 0)
        return res