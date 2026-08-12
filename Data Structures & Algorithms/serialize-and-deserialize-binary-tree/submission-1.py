# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # BFS as a string, 123NN45 makes sense here. val is forced to be an integer

        q = deque([root])
        self.res = ""

        while q:
            node = q.popleft()

            if node == None:
                self.res += "N"
            else:
                self.res += str(node.val)
                q.append(node.left)
                q.append(node.right)
        
        return self.res


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # We could either do a BFS to deserialize 1, 2, 4, 8 associated with each string
        # an alternative solution is that we can calculate the index of character for filling in the tree and perform DFS
        # the left child of a node is the index * 2, the right child is that plus 1.
        
        def dfsFill(ones_index):
            if ones_index - 1 >= len(data) or data[ones_index - 1] == None:
                return None

            else:
                node = TreeNode(data[ones_index - 1])
                node.left = dfsFill(2*ones_index)
                node.right = dfsFill(2 * ones_index + 1)

                return root

        return dfsFill(1)

