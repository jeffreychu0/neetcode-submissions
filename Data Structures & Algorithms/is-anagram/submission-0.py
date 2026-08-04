from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for char in s:
            freq1[char] += 1
        
        for char in t:
            freq2[char] += 1

        return freq1 == freq2

        