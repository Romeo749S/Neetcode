class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0,0,0]
        for i in nums:
            arr[i] += 1
        
        i = 0
        for n in range(len(arr)):
            for _ in range(arr[n]):
                nums[i] = n
                i += 1
        return nums
    
def main():
    sol = Solution()
    print(sol.sortColors([2,2,1,1,0,0,0]))

if __name__ == "__main__":
    main()