class Seq:
    def __init__(self, val):
        self.val = val
        self.next = 0 
        self.prev = 0 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Seq(homepage)
        self.tail = self.head
        

    def visit(self, url: str) -> None:
        new_page = Seq(url)
        new_page.prev = self.tail
        self.tail.next = new_page
        self.tail = self.tail.next
        

    def back(self, steps: int) -> str:
        i = 0
        while i != steps and self.tail.prev:
            i += 1
            self.tail = self.tail.prev
        if self.tail:
            return self.tail.val

    def forward(self, steps: int) -> str:
        i = 0
        while i != steps and self.tail.next:
            i += 1
            self.tail = self.tail.next
        if self.tail:
            return self.tail.val
        

def main():
    sol = BrowserHistory('leetcode')
    sol.visit('Linkedin')
    print(sol.back(1))
    print(sol.forward(1))

if __name__ == "__main__":
    main()