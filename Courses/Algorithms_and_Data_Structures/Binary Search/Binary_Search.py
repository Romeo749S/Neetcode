class Solution:
    def search(self, nums, target) -> int:
        def sear(s,e):
            if s > e :
                return -1
            elif nums[s] == target:
                return s
            m = int((s+e)/2)
            if target > nums[m]:
                return sear(m+1,e)
            elif target < nums[m]:
                return sear(s,m-1)
            else :
                return m
        return sear(0, len(nums) - 1)
    
def main():
    sol = Solution()
    print(sol.search([1,2,3,4,5],5))

if __name__ == "__main__":
    main()