class Solution:
    def isPalindrome(self, x: int) -> bool:


        lists = list(str(x))
        reversed = list(str(x))
        if lists[0] == "-":
            return False

        else:
            reversed.reverse()
            if reversed == lists:
                return True

            else:
                return False

if __name__ == '__main__':

    s = Solution()

    print(s.isPalindrome(10))
