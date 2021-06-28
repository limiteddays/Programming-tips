class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = []
        while(head): #head 라고 하면 그냥 head 까지만 하게 된다. 
            res.append(head.val)
            head = head.next
        return (res==res[::-1])


if __name__ == '__main__':

    c = ListNode(2,None)
    b = ListNode(1,c)

    sol = Solution()
    print(sol.isPalindrome(b))
