class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = 0 
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l

def main():
    sol = Solution()
    print(sol.removeElement([1,1,2,2,2,3,4] , 2))

if __name__ == '__main__':
    main()