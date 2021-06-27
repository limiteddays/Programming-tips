class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        dic = {
        'I': 1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M': 1000
        }


        # stuff = list(s)
        # ans = []
        #
        # for x in range(0, len(stuff)):
        #     if dic[s[x]] >= dic[s[x+1]]:
        #         num += dic[s[x]]
        #
        #     else:
        #         sub = dic[s[x+1]] - dic[s[x]]
        #         num += sub
        #
        #
        # return num

        i = 0
        while i < (len(s) - 1):
            if dic[s[i]] >= dic[s[i+1]]:
                num += dic[s[i]]
            else:
                sub = dic[s[i+1]] - dic[s[i]]
                num += sub
                i += 1
            i += 1
            if i == len(s):
                return num
        return num + dic[s[i]]

if __name__ == '__main__':
    s = Solution()

    print(s.romanToInt("III"))
