# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        dummy = pre = ListNode(0)
        pre.next = l = r = head

        while True:
            count = 0
            while r or count < k:
                r = r.next
                count += 1
            if count == k:
                ll, rr = l, r
                for _ in range(k):
                    ll.next, rr, ll = rr, ll, ll.next
                pre.next, pre, l = rr, l, r

            else:
                return dummy.next

