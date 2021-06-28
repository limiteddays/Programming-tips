class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        list1 = []
        current_node = l1
        while l1:

            if current_node.next == None:
                list1.append(current_node.val)
                break

            else:
                list1.append(current_node.val)
                current_node = current_node.next


        current_node = l2
        while l2:

            if current_node.next == None:
                list1.append(current_node.val)
                break

            else:
                list1.append(current_node.val)
                current_node = current_node.next


        list1.sort()

        if not list1:
            return None

        i = 0
        for x in list1:
            if i == 0:
                ans_node = ListNode(int(x),None)
                current_node = ans_node

            else:
                new_node = ListNode(int(x),None)
                current_node.next = new_node
                current_node = new_node

            i += 1

        return ans_node


if __name__ == '__main__':
    c = ListNode(1,None)
    b = ListNode(2,c)
    a = ListNode(3,b)

    sol = Solution()
    print(sol.mergeTwoLists(a,a))
