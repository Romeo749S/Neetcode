import math

class Solution:
    def minEatingSpeed(self, piles , h ) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            k = int((l + r) / 2)
            hours = 0
            for n in piles:
                hours += math.ceil(n/k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return  res 
