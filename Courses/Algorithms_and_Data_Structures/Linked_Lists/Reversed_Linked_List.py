class Nodes:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def Reversed_Linked_List(self, list1):
        prev, cur = None, list1

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        return prev