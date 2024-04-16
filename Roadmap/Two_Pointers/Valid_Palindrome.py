class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while not s[l].isalnum() and l < r :
                l += 1
            while not s[r].isalnum() and l < r :
                r -= 1
            if s[r].lower() != s[l].lower():
                return False
            r -= 1
            l += 1
        return True
    
def main():
    sol = Solution()
    print(sol.isPalindrome('anapana'))

if __name__ == "__main__":
    main()