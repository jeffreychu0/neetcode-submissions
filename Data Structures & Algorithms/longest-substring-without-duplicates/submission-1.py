class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1

        if len(s) <= 1:
            return len(s)

        seen = set([s[0]])
        ans = 0

        while r < len(s):
            if s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
                r += 1
                ans = max(ans, r - l)
        
        return ans