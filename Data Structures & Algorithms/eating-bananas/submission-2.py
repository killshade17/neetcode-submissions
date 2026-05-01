class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = max(piles)

        while l <= r:
            m = (l + r) // 2
            
            totalHours = 0
            for i in piles:
                totalHours += math.ceil(float(i)/m)
            if totalHours <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res 