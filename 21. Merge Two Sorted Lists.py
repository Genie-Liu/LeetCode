# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        rlt = ListNode(0)
        p = rlt
        while l1 is not None or l2 is not None:
            if l1 is None:
                while l2 is not None:
                    p.next = ListNode(l2.val)
                    l2 = l2.next
                    p = p.next
            elif l2 is None:
                while l1 is not None:
                    p.next = ListNode(l1.val)
                    l1 = l1.next
                    p = p.next
            else:
                if(l1.val < l2.val):
                    p.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    p.next = ListNode(l2.val)
                    l2 = l2.next
                p = p.next
        return rlt.next



