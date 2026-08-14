class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pt = 0
        max_pt = 0
        l = 0

        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                pt = prices[r] - prices[l]
                max_pt = max(pt, max_pt)
            else:
                l = r
        return max_pt