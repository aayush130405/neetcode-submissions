class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        pt = 0
        max_pt = 0

        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                pt = prices[r] - prices[l]
                max_pt = max(max_pt, pt)
            else:
                l = r
        return max_pt