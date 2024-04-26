class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def guess(m):
            if m > 3:
                return -1
            elif m < 3:
                return 1
            else :
                return 0
        
        s = 1
        while s <= n:
            m = (s+n) // 2
            if guess(m) == -1:
                n = m - 1
            elif guess(m) == 1:
                s = m + 1
            else:
                return m
def main():
    sol = Solution()
    print(sol.guessNumber(10))

if __name__ == "__main__":
    main()
    