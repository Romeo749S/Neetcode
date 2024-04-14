class MinStack(object):

    def __init__(self):
        self.length = 0
        self.capacity = 10
        self.arr = ['_'] * 10

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.arr[self.length] = val
        self.length += 1



    def pop(self):
        """
        :rtype: None
        """
        self.arr[self.length-1] = 0
        self.length -= 1
        

    def top(self):
        """
        :rtype: int
        """
        return self.arr[self.length-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.arr
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.push(0)
obj.push(3)
obj.push(0)
obj.pop()
obj.pop()
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_4, param_3)