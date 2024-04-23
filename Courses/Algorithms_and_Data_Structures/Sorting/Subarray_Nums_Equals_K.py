class Solution:
    def findKthLargest(self, nums, k) -> int:
        k = len(nums) - k
        def select(s,e):
            pivot = nums[e]
            left = s
            for i in range(s,e):
                if nums[i] <= pivot:
                    nums[i], nums[left] = nums[left], nums[i]
                    left += 1
            nums[left], nums[e] = nums[e], nums[left]
            if k < left:
                return select(s, left-1)
            elif k > left:
                return select(left+1, e)
            else:
                return nums[left]
        return select(0, len(nums)-1)