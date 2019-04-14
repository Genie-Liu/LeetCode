# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        s = t = head
        sp = s
        for i in range(n-1):
            if t is None:
                return
            t = t.next

        while t.next is not None:
            sp = s
            s = s.next
            t = t.next

        if s == head:
            if t != head:
                return head.next
            else:
                return None
        elif s.next is None:
            sp.next = None
            return head
        else:
            sp.next = s.next
            return head


