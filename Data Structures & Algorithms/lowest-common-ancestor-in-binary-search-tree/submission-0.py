# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # perform a postorder traversal, return whether P or Q is found in the nodes
        # As you iterate, return immediately as you find both P and Q, this is the lowest common ancestor

        ans = None

        def postorder(root):
            nonlocal ans
            left = False
            right = False
            # output schema: (FALSE, FALSE) relative to P and Q

            if not root:
                return (False, False)

            left_res = postorder(root.left)
            right_res = postorder(root.right)

            if root.val == p.val:
                left = True
            elif root.val == q.val:
                right = True

            if (left_res[0] or right_res[0] or left) and (left_res[1] or right_res[1] or right):
                print(root.val)
                if ans == None:
                    ans = root

            return (left_res[0] or right_res[0] or left, left_res[1] or right_res[1] or right)
        
        postorder(root)

        return ans