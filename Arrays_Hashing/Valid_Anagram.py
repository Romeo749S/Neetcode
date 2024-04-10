class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for n in s:
            if n not in t:
                return False
        return len(t) == len(s)
    

def main():
    sol = Solution()
    print(sol.isAnagram('aksa', 'saka'))

if __name__ == "__main__":
    main()