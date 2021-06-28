class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        s = list(s)
        longest = 0

        for x in range (0, len(s)):
            j = 0
            while j < 27:

                if alphabet[j] == s[x]:
                    break

                j += 1

            i = x
            current_alpha = 0

            # print(j, i)

            while i < len(s):

                if s[i] == alphabet[j]:

                    current_alpha += 1
                    i += 1
                    j += 1
                    continue

                else:
                    break

            if current_alpha > longest:
                longest = current_alpha

            else:
                continue

        return longest


if __name__ == '__main__':
    s = Solution()

    print(s.lengthOfLongestSubstring("abcabcbb"))
