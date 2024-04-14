class Solution(object):
    def validation(self, strp):
        res = []
        for i in strp:
            if i in ['[', '(', '{']:
                res.append(i)
            elif len(res) == 0:
                return False
            elif i == ')' and res[-1] == '(':
                res.pop()
            elif i == ']' and res[-1] == '[':
                res.pop()
            elif i == '}' and res[-1] == '{':
                res.pop()
            else :
                return False
        return True
    
def main():
    sol = Solution()
    print(sol.validation('[][[[[[()]]]]]'))

if __name__ == '__main__':
    main()