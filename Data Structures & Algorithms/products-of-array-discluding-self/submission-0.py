class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        answer = []

        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]
        
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                continue
            else:
                right[i] = right[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            answer.append(left[i] * right[i])

        return answer
        