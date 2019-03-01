package src;

/**
 * Enables removal of targets from a linked list.
 */
public class Solution {

    /**
     * Linked lists are composed of these nodes.
     */
    public static class ListNode {
        public ListNode next;
        public int val;


        public ListNode(int x) { val = x; }
    }

    /**
     * Remove targets from a linked list.
     * @param head The linked list
     * @param val The target
     * @return A Linked List with no occurrences of the value given by target
     */
    public static ListNode removeElements(ListNode head, int val) {
        //Pre-processing: make sure first element in the list is valid
        while(head != null && head.val == val) {
            head = head.next;
        }
        // 0 nodes
        if(head == null) {
            return null;
        }
        // 1 node
        if(head.next == null) {
            if(head.val == val) {
                return null;
            } else {
                return head;
            }
        }
        //2+ nodes. loop invariant: 'prev' references a node that will be kept,
        //while 'curr' must be examined and possibly removed,
        ListNode prev = head;
        ListNode curr = head.next;
        while(curr != null) {
            //there are more elements in the list, curr is underconsideration
            curr = eval_curr(val, prev, curr);
            //prev is a valid node, curr is either valid or null
            if(curr != null) {
                prev = curr;
                curr = curr.next;
            }
        }
        return head;
//        //Other way to construct the 'while' loop to traverse the link-list,
//        //uses a different invariant.
//        ListNode prev = head;
//        ListNode curr = head.next;
//        eval_curr(val, prev, curr);
//
//        //body. prev and curr point at nodes which will not be removed.
//        while(curr.next != null) {
//            prev = curr;
//            curr = curr.next;
//            eval_curr(val, prev, curr);
//        }
    }

    public static ListNode removeElements2(ListNode head, int val) {
        //Pre-processing: make sure first element in the list is valid
        while(head != null && head.val == val) {
            head = head.next;
        }
        // 0 nodes
//        if(head == null) {
//            head = null;
//            return null;
//        }
        // 1 node
//        if(head.next == null) {
//            if(head.val == val) {
//                return null;
//            } else {
//                return head;
//            }
//        }
        //2+ nodes. loop invariant: 'prev' references a node that will be kept,
        //while 'curr' must be examined and possibly removed,
        ListNode prev = head;
        while(prev != null) {
            //there are more elements in the list, curr is underconsideration
            prev = eval_curr2(val, prev);
            //prev is a valid node, prev.next is either valid or null
            prev = prev.next;
        }
        return head;
    }

    /**
     * Updates curr until it points to a valid node or to null.
     * @param val The integer value to be removed from the linked list
     * @param prev References a node that will not be removed.
     * @param curr References a node that may or may not be removed.
     * @return A reference to a node which will be kept and follows prev, or
     * null. Note: The node prev is modified so that it points to the new
     * curr or to null.
     */
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

    private static ListNode eval_curr2(int val, ListNode prev) {
        while(prev.next != null && prev.next.val == val) {
            prev.next = prev.next.next;
        }
        return prev;
    }
}
