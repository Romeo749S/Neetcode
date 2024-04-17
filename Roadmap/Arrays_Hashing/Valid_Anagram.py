class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash = dict()
        for i in s:
            if i not in hash:
                hash[i] = 0
            hash[i] += 1
        for i in t:
            if i not in hash:
                return False  
            hash[i] -= 1
        for i in hash:
            if hash[i] != 0:
                return False
        return True
        
    

def main():
    sol = Solution()
    print(sol.isAnagram('aksa', 'saka'))

if __name__ == "__main__":
    main()