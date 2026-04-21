# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None: return 0

        self.count = 0

        def helper(root: TreeNode, currmax):
            if root is None: return

            if root.val >= currmax:
                self.count += 1
                currmax = root.val
            
            helper(root.left, currmax)
            helper(root.right, currmax)
        

        helper(root, float('-inf'))

        return self.count



        