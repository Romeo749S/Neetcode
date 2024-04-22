class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, l, r = L, 0, 0
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    arr[i] = left[l]
                    l += 1
                else:
                    arr[i] = right[r]
                    r += 1
                i += 1 
            while l < len(left):
                arr[i] = left[l]
                l += 1
                i += 1
            while r < len(right):
                arr[i] = right[r]
                r += 1
                i += 1
            

        def mergeSort(arr, l, r):
            if l == r:
                return arr
            
            m = int((l+r)/2)
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r,)
            return arr

        return mergeSort(nums, 0, len(nums) - 1)
    

def main():
    sol = Solution()
    print(sol.sortArray([2,4,5,6]))

if __name__ == "__main__":
    main()
    