class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution(object):
    def __init__(self):
        self.head = Node(1)
        self.tail = self.head
        self.tail.next = Node(2)
        self.tail.next.next = Node(3)
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        front = head.next
        front.next = head
        head.next = None
        return new_head.data
    
def main():
    sol = Solution()
    print(sol.reverseList(sol.head))

if __name__ == "__main__":
    main()
    
