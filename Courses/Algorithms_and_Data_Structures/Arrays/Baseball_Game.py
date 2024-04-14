class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = []
        for i in operations:
                if i.strip('-').isnumeric() :
                    res.append(int(i))
    
                elif i =='D':
                    res.append(res[-1] * 2)
           
                elif i == 'C':
                    res.pop()
  
                elif i == '+':
                    res.append(res[-1] + res[-2])
                  
        return sum(res)
    
def main():
    sol = Solution()
    print(sol.calPoints(["5","-2","4","C","D","9","+","+"]))

if __name__ == '__main__':
    main()