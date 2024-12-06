# Given the head of a linked list, remove the nth node
# from the end of the list and return its head.
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
# Input: head = [1], n = 1
# Output: []
# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# Follow up: Could you do this in one pass?
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        trav = delay_trav = head
        if trav.next == None:
            head = None
            return head
        while(trav.next is not None):
            if n <= 0:
                delay_trav = delay_trav.next
            else:
                n -= 1
            trav = trav.next
        if n == 1:
            head = head.next
        if delay_trav.next is not None:
            delay_trav.next = delay_trav.next.next
        return head

def printLinkedList(head):
    trav = head
    print("Head -> ", end="")
    while trav is not None:
        print(trav.val, end="")
        if trav.next is not None:
            print(" -> ", end="")
        trav = trav.next

def run(head, n):
    print("Before: ")
    printLinkedList(head)
    sol = Solution()
    head = sol.removeNthFromEnd(head, n)
    print("\nAfter: ")
    printLinkedList(head)

def main():
    head1 = ListNode(1,
                    ListNode(2,
                             ListNode(3,
                                      ListNode(4, ListNode(5)))))
    print("case 1:")
    run(head1, 1)
    print("\ncase 2:")
    run(ListNode(1), 1)
    print("\ncase 3:")
    run(ListNode(1, ListNode(2)), 1)

main()
