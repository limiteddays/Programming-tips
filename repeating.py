class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        s = list(s)
        longest = ""

        for x in range (0, len(s)):
            j = 0
            alpha_index = 0
            while j < 27:

                if alphabet[j] == s[x]:
                    alpha_index = j
                    break


            while s:
                
                if
