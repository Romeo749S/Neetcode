class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.right = None
        self.left = None
class TreeMap:
    def __init__(self):
        self.root = None
        self.res = []
        self.arr = []
    

    def trav(self, root, key, val):
        if not root:
            return Node(key, val)
        if key > root.key:
            root.right = self.trav(root.right, key, val)
        elif key < root.key:
            root.left = self.trav(root.left, key, val)
        elif key == root.key:
            root.val = val
        return root

    def trav2(self, root, key):
        if not root:
            return
        self.trav2(root.left, key)
        if root.key == key:
            self.res.append(root)
            return
        self.trav2(root.right, key)

    def trav3(self, root):
        if not root:
            return
        self.trav3(root.left)
        self.arr.append(root.key)
        self.trav3(root.right)

    def trav4(self, root, key):
        if not root:
            return None
        if key > root.key:
            root.right = self.trav4(root.right, key)
        elif key < root.key:
            print(root.key)
            root.left = self.trav4(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.key = cur.key
                root.right = self.trav4(root.right,cur.key)
                return root
            return root

            
        
    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = Node(key, val)
        else:
            self.trav(self.root, key, val)


    def get(self, key: int) -> int:
        self.trav2(self.root, key)
        if not self.res:
            return -1
        else:
            return self.res.pop().val

    def getMin(self) -> int:
        if not self.root:
            return -1
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur.val

    def getMax(self) -> int:
        if not self.root:
            return -1
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur.val

    def remove(self, key: int) -> None:
        self.root = self.trav4(self.root, key)
        
    def getInorderKeys(self) -> List[int]:
        self.trav3(self.root)
        g = self.arr.copy()
        self.arr.clear()
        return g