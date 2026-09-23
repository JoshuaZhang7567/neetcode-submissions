import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1
        f = max(piles)
        ans = f

        while s <= f:

            m = (f+s)//2

            count = 0
            for p in piles:
                count += math.ceil(p/m)

            if count > h:
                s = m + 1
            else:
                ans = m
                f = m - 1
                

        return ans