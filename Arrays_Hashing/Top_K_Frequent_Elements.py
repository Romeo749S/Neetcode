class Solution(object):
    def topKFrequent1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash = {}
        res = []
        for n in nums:
            hash[n] = 1 + hash.get(n, 0)
        sub = [n for n in sorted(hash.values())[::-1]]

        for n in range(k):
            for j in hash:
                if hash[j] == sub[n]:
                    res.append(j)
                    hash.pop(j)
                    break
        return res
    
    def topKFrequent2(self, nums, k):
        hash = {}
        res = []
        array = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            hash[n] = 1 + hash.get(n, 0)
        for i, j in hash.items():
            array[j].append(i)
        for n in range(len(array))[::-1]:
            for j in array[n]:
                res.append(j)
                if len(res) == k:
                    return res


        

def main():
    sol = Solution()
    print(sol.topKFrequent2([1,],1))

if __name__ == "__main__":
    main()