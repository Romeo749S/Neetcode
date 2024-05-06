# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root :
            return []
        n = -1
        res = []
        queue = deque() 
        queue.append(root)
        while len(queue) > 0:
            n += 1
            res.append([])
            for _ in range(len(queue)):
                cur = queue.popleft()
                res[n].append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res