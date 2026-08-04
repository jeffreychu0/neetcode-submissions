from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_map = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            
            for c in s:
                freq[ord(c) - ord('a')] += 1
            
            ans_map[tuple(freq)].append(s)

        return list(ans_map.values())


