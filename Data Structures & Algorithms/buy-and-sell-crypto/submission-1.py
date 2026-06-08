#import numpy as np
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b,s = 0,1
        p = 0

        while s < len(prices):
            if prices[b]<prices[s]:
                p = max(p,(prices[s]-prices[b]))
            else:
                b = s
            s += 1
        return p
