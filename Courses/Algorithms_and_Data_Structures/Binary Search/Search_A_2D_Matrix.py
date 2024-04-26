class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for n in range(len(matrix)):
            if matrix[n][-1] >= target:
                res = matrix[n]
                l, r = 0 , len(res) - 1
                while l <= r:
                    m = (r+l) // 2
                    if res[m] < target:
                        l = m + 1
                    elif res[m] > target:
                        r = m - 1 
                    else :
                        return True
                return False
        return False
        
def main():
    sol = Solution()
    print(sol.searchMatrix([[1,2,3,4,5],[6,7,8,9,10]],5))

if __name__ == "__main__":
    main()