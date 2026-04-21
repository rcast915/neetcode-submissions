# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        def helper(root: Optional[TreeNode], minval, maxval):
            if root is None:
                return True
            
            if root.val > minval and root.val < maxval:
                return helper(root.left, minval, root.val) and helper(root.right, root.val, maxval)
            
            else:
                return False


        return helper(root, float('-inf'), float('inf'))
        