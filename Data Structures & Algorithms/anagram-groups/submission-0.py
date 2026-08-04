from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        ans = []

        for string in strs:
            freq = [0] * 26

            print(freq)

            for char in string:
                freq[ord(char) - ord("a")] += 1
            
            if tuple(freq) in my_map:
                ans[my_map[tuple(freq)]].append(string)
            else:
                ans.append([string])
                my_map[tuple(freq)] = len(ans) - 1
            
        return ans

