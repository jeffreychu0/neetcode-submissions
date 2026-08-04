class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0 for _ in range(26)]
        s2_count = [0 for _ in range(26)]
        matches = 0
        
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1

        l = 0
        r = len(s1)
        
        for char in s2[l:r]:
            s2_count[ord(char) - ord('a')] += 1

        for i in range(26):
            matches += 1 if s1_count[i] == s2_count[i] else 0

        while r < len(s2):
            print(matches)
            if matches >= 26:
                return True

            char_removed = s2[l]
            char_added = s2[r]

            l += 1
            r += 1

            s2_count[ord(char_removed) - ord('a')] -= 1
            s2_count[ord(char_added) - ord('a')] += 1

            if s1_count[ord(char_added) - ord('a')] == s2_count[ord(char_added) - ord('a')]:
                matches += 1
            elif s1_count[ord(char_added) - ord('a')] + 1 == s2_count[ord(char_added) - ord('a')]:
                matches -= 1

            if s1_count[ord(char_removed) - ord('a')] == s2_count[ord(char_removed) - ord('a')]:
                matches += 1
            elif s1_count[ord(char_removed) - ord('a')] - 1 == s2_count[ord(char_removed) - ord('a')]:
                matches -= 1
            
        return matches == 26

            
 


