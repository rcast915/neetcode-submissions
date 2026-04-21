# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        def helper(node):
            if not node:
                return "None"
            return f"{node.val},{helper(node.left)},{helper(node.right)}"

        return helper(root)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        def helper(data_list):
            if data_list[0] == "None":
                data_list.pop(0)
                return None

            node = TreeNode(int(data_list.pop(0)))
            node.left = helper(data_list)
            node.right = helper(data_list)
            return node

        data_list = data.split(',')
        return helper(data_list)