class Node:
    def __init__(self, data):
        self.data = data
        self.next = 0
class MyStack:

    def __init__(self):
       self.head = Node(-1)
       self.tail = self.head 

    def push(self, x: int) -> None:
        new_node = Node(x)
        self.tail.next = new_node
        self.tail = self.tail.next

    def pop(self) -> int:
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
        x = cur.next
        if self.tail == cur.next:
            self.tail = cur
        cur.next = cur.next.next
        return x.data
        

    def top(self) -> int:
        return self.tail.data

    def empty(self) -> bool:
        if self.head.next:
            return False
        return True
    
def main():
    sol = MyStack()
    sol.push(1)
    sol.push(2)
    print(sol.top())
    print(sol.pop())
    print(sol.top())
    print(sol.pop())
    print(sol.top())
    print(sol.empty())

if __name__ == "__main__":
    main()