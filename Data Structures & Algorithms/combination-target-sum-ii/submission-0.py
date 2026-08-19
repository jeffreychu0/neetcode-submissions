class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        
        def dfs(idx, curr, total):
            # Base Case
            if total == target:
                res.append(curr.copy())
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break

                curr.append(candidates[i])
                dfs(i + 1, curr, total + candidates[i])
                curr.pop()
        
        dfs(0, [], 0)
        return res