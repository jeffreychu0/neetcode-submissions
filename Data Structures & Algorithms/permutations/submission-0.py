class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, rem):
            if not rem:
                res.append(curr.copy())
                return
            
            for elem in list(rem):
                rem.remove(elem)
                curr.append(elem)
                dfs(curr, rem)

                rem.add(elem)
                curr.pop()
        
        dfs([], set(nums))
        return res
