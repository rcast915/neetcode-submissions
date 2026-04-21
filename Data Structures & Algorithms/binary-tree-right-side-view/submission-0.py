# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        q = deque()
        q.append(root)

        result = []
        while q:
            level = []
            levellen = len(q)

            for _ in range(levellen):
                node = q.popleft()
                level.append(node.val)

                if node.left is not None:
                    q.append(node.left)
                
                if node.right is not None:
                    q.append(node.right)
                
            result.append(level[-1])

        return result

        