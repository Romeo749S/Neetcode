class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        hash = {}
        for n in range(1, len(nums)):
            hash[n] = nums[n]
        nums.sort()
        for n , a in enumerate(nums):
            if n > 0 and nums[n] == nums[n-1]:
                continue

            l, r = n+1 , len(nums) - 1
            while r > l:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
    

def main():
    sol = Solution()
    print(sol.threeSum([1,1,2,6,10,-11]))

if __name__ == "__main__":
    main()