class Solution:
    def maxProfit(self, pcs: List[int]) -> int:
        maxx = 0
        p = 0
        l = 0

        for r in range(len(pcs)):
            if pcs[r] > pcs[l]:
                p = pcs[r] - pcs[l]
                maxx = max(p, maxx)
            else:
                l = r
        return maxx