# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from queue import PriorityQueue


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = PriorityQueue()
        dummy = ListNode(None)
        current = dummy
        for i in range(len(lists)):
            if lists[i]:
                q.put((lists[i].val, i, lists[i]))
        while not q.empty():
            _, idx, current.next = q.get()
            current = current.next
            if current.next:
                q.put((current.next.val, idx, current.next))
        return dummy.next
