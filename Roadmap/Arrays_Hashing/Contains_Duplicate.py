class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dist_list = list()
        for n in nums:
            if n not in dist_list:
                dist_list.append(n)
        return len(dist_list) != len(nums)

def main():
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,4,5,5]))

if __name__ == "__main__":
    main()