package src;


public class Solution {
    public static class ListNode {
        public ListNode next;
        public int val;


        public ListNode(int x) { val = x; }
    }

    public static ListNode removeElements(ListNode head, int val) {
        //Make sure first element in the list is valid
        while(head != null && head.val == val) {
            head = head.next;
        }

        // 0
        if(head == null) {
            return null;
        }

        //1
        if(head.next == null) {
            if(head.val == val) {
                return null;
            } else {
                return head;
            }
        }

        //body. invarient: prev is legit, current we might need to get rid of.
        //invarient is easy to initialize
        ListNode prev = head;
        ListNode curr = head.next;
        while(curr != null) {
            curr = eval_curr(val, prev, curr);
            //prev is a legit node, curr is either legit or null
            if(curr != null) {
                prev = curr;
                curr = curr.next;
            }
        }

        //initialize invarient - the hard part.
//        ListNode prev = head;
//        ListNode curr = head.next;
//        eval_curr(val, prev, curr);

        //body. prev and curr point at legit nodes.
//        while(curr.next != null) {
//            prev = curr;
//            curr = curr.next;
//            eval_curr(val, prev, curr);
//        }

        return head;
    }

    // updates curr until it points to a valid node or it is null.
    // returns: the new curr.
    private static ListNode eval_curr(int val, ListNode prev, ListNode curr) {
        while(curr != null && curr.val == val) {
            if(curr.next == null) {
                prev.next = null;
                curr = null;
            } else {
                prev.next = curr.next;
                curr = curr.next;
            }
        }
        return curr;
    }
}
