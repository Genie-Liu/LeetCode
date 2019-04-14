/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if(l1 == null) return l2;
        if(l2 == null) return l1;
        int c = 0;
        int v1, v2, v;
        ListNode rlt = new ListNode(0);
        ListNode p = rlt;
        while(l1 != null || l2 != null) {
            v1 = v2 = 0;
            if(l1 != null){
                v1 = l1.val;
                l1 = l1.next;
            } 
            if(l2 != null){
                v2 = v2.val;
                l2 = l2.next;
            }
            v = v1 + v2 + c;
            c = v / 10;
            p.next = new ListNode(v % 10);
            p = p.next;
        }
        if(c != 0)
            p.next = new ListNode(c);

        return rlt.next;
    }
}