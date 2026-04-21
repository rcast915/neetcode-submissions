# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.curr = float('-inf')

        def helper(root):
            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            l = max(left, 0)
            r = max(right, 0)
            

            self.curr = max(self.curr, l + r + root.val )
            return max(l,r) + root.val

        helper(root)

        return self.curr
            

        