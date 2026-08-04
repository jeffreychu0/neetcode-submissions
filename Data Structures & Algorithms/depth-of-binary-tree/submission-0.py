# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        def inOrder(node, height):
            if not node:
                return height
            return max(inOrder(node.left, height + 1), inOrder(node.right, height + 1))

        return inOrder(root, 0)