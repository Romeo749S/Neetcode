class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in range(len(nums)):
            nums.append(nums[n])
        return nums
    
def main():
    sol = Solution()
    print(sol.getConcatenation([1,2,3]))

if __name__ == '__main__':
    main()