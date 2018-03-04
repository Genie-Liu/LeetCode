# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            self.swapNextPair(curr)
            curr = curr.next.next
        return dummy.next

    def swapNextPair(self, head):
        n1 = head.next
        n2 = n1.next
        head.next = n2
        n1.next = n2.next
        n2.next = n1


