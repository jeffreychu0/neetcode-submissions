class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_pairs = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []

        for char in s:

            if char in parenthesis_pairs.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                pair_val = stack.pop()
                if parenthesis_pairs[char] != pair_val:
                    return False
        
        return len(stack) == 0
            