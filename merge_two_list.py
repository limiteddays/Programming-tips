class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        list1 = []
        list2 = []

        i = 0
        current_node_1 = l1
        current_node_2 = l2
        while True:
            if i == 50:
                break

            else:
                list1.append(current_node_1.val)
                list2.append(current_node_2.val)
                current_node_1 = current_node_1.next
                current_node_2 = current_node_2.next
                i += 1

        list3 = list1 + list2
        return sort(list3)

if __name__ == '__main__':

    s = Solution()

    s.mergeTwoLists([1,2,3,4], [1,2,3,3])
