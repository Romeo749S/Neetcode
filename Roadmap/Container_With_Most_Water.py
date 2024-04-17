class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = min(height[l] , height[r]) * (r - l)
            res = max(res, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res
    
def main():
    sol = Solution()
    print(sol.maxArea([1,2,3,3,4,5,6,7,8]))

if __name__ == "__main__":
    main()