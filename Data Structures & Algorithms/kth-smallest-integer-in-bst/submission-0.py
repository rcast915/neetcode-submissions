# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    curr = 0
    val = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(root: Optional[TreeNode]):
            
            if root.left:
                helper(root.left)
            
            self.curr += 1

            if self.curr == k:
                self.val = root.val
            
            if root.right:
                helper(root.right)
        
        if root is None: return None
        helper(root)
        return self.val


        
