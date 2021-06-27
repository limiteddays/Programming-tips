class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        temp1 = ""
        temp2 = ""
        current_node_1 = l1
        current_node_2 = l2
        while True:

            if current_node_1.next == None:
                temp1 = str(current_node_1.val) + temp1
                break

            else:
                temp1 = str(current_node_1.val) + temp1
                current_node_1 = current_node_1.next

        while True:

            if current_node_2.next == None:
                temp2 = str(current_node_2.val) + temp2
                break

            else:
                temp2 = str(current_node_2.val) + temp2
                current_node_2 = current_node_2.next

        # ans_list = (list(val1 + val2)).reverse()

        temp3 = int(temp1) + int(temp2)
        temp3 = str(temp3)[::-1]

        i = 0
        for x in temp3:
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
    print(sol.addTwoNumbers(a,a))
