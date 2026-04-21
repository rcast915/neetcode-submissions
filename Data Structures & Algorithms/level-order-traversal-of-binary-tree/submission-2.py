# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []  # Return an empty list if the root is None

        q = deque()
        q.append(root)
        result = []

        while q:
            levellen = len(q)
            level = []
            for _ in range(levellen):
                node = q.popleft()
                level.append(node.val)  # Append the current node's value to the level list

                # Ensure left child is appended before the right child to maintain order
                if node.left is not None:
                    q.append(node.left)
                
                if node.right is not None:
                    q.append(node.right)

            if level:
                result.append(level)  # Append the current level to the result list

        return result