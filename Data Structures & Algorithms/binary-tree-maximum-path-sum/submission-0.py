# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # perform a postorder (left, right, middle)

        # each return should either be 0, or the max possible value assuming minimum 1 path

        # at each node, assume we are the root, then we can add both paths together

        # store maximum as a result.

        self.res = root.val #if we have no children, this should be the max

        def postOrder(root):

            if not root:
                return 0

            left_max = postOrder(root.left)
            right_max = postOrder(root.right)

            # perform the root analysis
            self.res = max(self.res, left_max + right_max + root.val)
            
            # return a minimum between 0 (no use if negative) and the paths max possible value

            return max(0, max(left_max + root.val, right_max + root.val))

        postOrder(root)
        return self.res
