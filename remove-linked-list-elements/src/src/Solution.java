package src;


public class Solution {
    public static class ListNode {
        public ListNode next;
        public int val;


        public ListNode(int x) { val = x; }
    }

    public static ListNode removeElements(ListNode head, int val) {
        // 0
        if(head == null) {
            return null;
        }

        //1
        if(head.next == null) {
            return head;
        }

        //initialize invarient - the hard part.
        ListNode prev = head;
        ListNode curr = head.next;
        eval_curr(val, prev, curr);

        //body. prev and curr point at legit nodes.
        while(curr.next != null) {
            prev = curr;
            curr = curr.next;
            eval_curr(val, prev, curr);
        }

        return head;
    }

    private static void eval_curr(int val, ListNode prev, ListNode curr) {
        while(curr != null && curr.val == val) {
            if(curr.next == null) {
                prev.next = null;
            } else {
                prev.next = curr.next;
                curr = curr.next;
            }
        }
    }
}
