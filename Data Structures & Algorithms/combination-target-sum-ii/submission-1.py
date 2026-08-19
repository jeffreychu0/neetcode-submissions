class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        # if we choose to deny adding an element, we need to never add that element at any point of the new tree

        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            backtrack(i + 1, curr, total + candidates[i])
            
            curr.pop()
            j = i

            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            
            backtrack(j, curr, total)
        
        backtrack(0, [], 0)
        return res