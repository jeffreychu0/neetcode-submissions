# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        ret = True

        def inorder(root):
            nonlocal ret
            nonlocal prev

            if not root:
                return

            inorder(root.left)

            if prev is None:
                prev = root.val
            elif root.val <= prev:
                ret = False
            prev = root.val
            
            inorder(root.right)
        
        inorder(root)

        return ret