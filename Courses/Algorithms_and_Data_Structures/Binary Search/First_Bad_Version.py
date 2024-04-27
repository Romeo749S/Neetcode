class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isBadVersion(m):
            if m >= 4:
                return True
            return False
        l, r = 1, n
        while l <= r:
            m = int((l+r) / 2)
            if not isBadVersion(m):
                l = m + 1
            elif isBadVersion(m-1):
                r = m - 1
            else :
                return m


def main():
    sol = Solution()
    print(sol.firstBadVersion(20))

if __name__ == "__main__":
    main()