from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = 0

        while left <= right:
            hours_needed = 0
            mid = (left + right) // 2

            for i in piles:
                hours_needed += ceil(i/mid)
            
            if hours_needed <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans