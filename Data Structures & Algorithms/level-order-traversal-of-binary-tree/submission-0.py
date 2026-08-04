# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0)])
        
        ans = []

        if not root:
            return ans

        while queue:
            params = queue.popleft()

            while len(ans) <= params[1]:
                ans.append([])

            if params[0].left:
                queue.append((params[0].left, params[1] + 1))
            
            if params[0].right:
                queue.append((params[0].right, params[1] + 1))

            ans[params[1]].append(params[0].val)
        
        return ans
