from collections import defaultdict
class Solution(object):
    def groupAnagrams1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash = {}
        for n in strs:
            sorted_word = ''.join(sorted(n))
            if sorted_word not in hash:
                hash[sorted_word] = []
            hash[sorted_word].append(n)
        return list(hash.values())
    def groupAnagrams2(self, strs):
        hash = defaultdict(list)
        for n in strs:
            count = [0] * 26
            for i in n:
                count[ord(i) - ord('a')] += 1
            hash[tuple(count)].append(n)
        return list(hash.values())

    
def main():
    sol = Solution()
    print(sol.groupAnagrams2(["eat","tea","tan","ate","nat","bat"]))

if __name__ == "__main__":
    main()