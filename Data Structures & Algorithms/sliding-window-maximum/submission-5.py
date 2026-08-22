from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        l = 0
        result = []

        for r in range(len(nums)):
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)
            while dq and dq[0] < l:
                dq.popleft()
            
            if r - l + 1 == k:
                result.append(nums[dq[0]])
                l += 1
        return result