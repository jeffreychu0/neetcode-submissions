from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)

        for string in strs:
            freq = [0] * 26

            for char in string:
                freq[ord(char) - ord("a")] += 1
            
            my_map[tuple(freq)].append(string)
            
        return list(my_map.values())

