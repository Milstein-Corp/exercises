import org.junit.Test;
import src.Solution.ListNode;
import src.Solution;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

import static junit.framework.TestCase.fail;

//Tests for class Solution
public class Tests {
    /**
     * Produce a default linked list
     * @return a linked list with 10 elements in it.
     */
    public ListNode dummy_list() {
        ListNode head = new ListNode(0);
        ListNode curr = head;

        for(int i = 1; i < 10; i++) {
            ListNode n = new ListNode(i);
            curr.next = n;
            curr = curr.next;
        }

        return head;
    }

    /**
     * Produce a linked list
     * @param a Desired contents for your linked list
     * @return A linked list with with contents of Integer array a.
     */
    public ListNode linked_list(Integer[] a) {

        if(a == null) {
            return null;
        }

        ArrayList<Integer> i = new ArrayList<Integer>(Arrays.asList(a));
        Iterator<Integer> it = i.iterator();

        ListNode head = new ListNode(it.next());
        ListNode current = head;

        while(it.hasNext()) {
            int b = it.next();
            ListNode l = new ListNode(b);
            current.next = l;
            current = l;
        }

        return head;
    }

    /**
     * Print your linked list to std output for examination
     * @param l A linked list
     */
    public void print_ll(ListNode l) {
        while(l != null) {
            System.out.println(l.val);
            l = l.next;
        }
    }

    /**
     * Are these two linked lists exactly the same?
     * @param l1 One linked list
     * @param l2 Another linked list
     */
    public void lists_match(ListNode l1, ListNode l2) {
        while(l1 != null && l2 != null) {
            assert(l1.val == l2.val);
            l1 = l1.next;
            l2 =l2.next;
        }
        assert(l1 == null && l2 == null); 
    }

    /**
     * Verfity that a target value is removed from a linked list,
     * everywhere it occurs.
     * @param raw A linked list
     * @param target The value to be removed from the linked list
     * @param desired_result
     */
    private void verify_removal(
            Integer[] raw, Integer target,Integer[] desired_result) {
        ListNode raw_ll = linked_list(raw);
        ListNode result = Solution.removeElements(raw_ll, target);
        ListNode desired_result_ll = linked_list(desired_result);
        lists_match(result, desired_result_ll);
    }

    /**
     * Blackbox test for lists_match(..)
     */
    @Test(timeout=1000)
    public void test_lists_match() {
        ListNode l1 = linked_list(new Integer[]{0, 0, 0, 2, 0});
        ListNode l2 = linked_list(new Integer[]{0, 0, 0, 2, 0});
        ListNode l3 = linked_list(new Integer[]{0, 0, 1, 2, 0});
        ListNode l4 = linked_list(new Integer[]{0, 0, 1, 2, 0});
        ListNode l5 = linked_list(new Integer[]{0});
        ListNode l6 = linked_list(new Integer[]{0});

        lists_match(l1, l2);
        lists_match(l3, l4);
        lists_match(l5, l6);

        l1 = linked_list(new Integer[]{0, 0, 0, 2, 1});
        l2 = linked_list(new Integer[]{0, 0, 0, 2, 0});
        l3 = linked_list(new Integer[]{0, 0, 0, 2, 0});
        l4 = linked_list(new Integer[]{0, 0, 1, 2, 0});
        l5 = linked_list(new Integer[]{1, 4});
        l6 = linked_list(new Integer[]{1});


        try {
            lists_match(l1, l2);
            throw new UnknownError();
        } catch (AssertionError e) {}
        try {
            lists_match(l3, l4);
            throw new UnknownError();
        } catch (AssertionError e) {}
        try {
            lists_match(l5, l6);
            throw new UnknownError();
        } catch (AssertionError e) {}
    }

    /**
     * Blackbox test for Solution.removeElements(..), focusing on input lists
     * of size 2 or less.
     */
    @Test(timeout=1000)
    public void small_lists() {

        Integer[] raw;
        Integer target;
        Integer[] result;

        //empty initial list
        target = 0;
        raw = null;
        result = null;
        verify_removal(raw, target, result);

        //size=1, remove it
        target = 0;
        raw = new Integer[] {0};
        result = null;
        verify_removal(raw, target, result);

        //size=1, leave it
        target = 4;
        raw = new Integer[] {0};
        result = new Integer[] {0};
        verify_removal(raw, target, result);

        //size=2, remove nothing
        target = 4;
        raw = new Integer[] {0, 2};
        result = new Integer[] {0, 2};
        verify_removal(raw, target, result);

        //size=2, remove front
        target = 0;
        raw = new Integer[] {0, 2};
        result = new Integer[] {2};
        verify_removal(raw, target, result);

        //size=2, remove end
        target = 2;
        raw = new Integer[] {0, 2};
        result = new Integer[] {0};
        verify_removal(raw, target, result);
    }

    /**
     * Blackbox test for Solution.removeElements(..), focusing on input lists
     * around size 10.
     */
    @Test(timeout=1000)
    public void reg_lists() {

        Integer[] raw = new Integer[] {0, 1, 2, 3, 4, 5, 6};
        Integer target;
        Integer[] result;

        target = 0;
        result = new Integer[] {1, 2, 3, 4, 5, 6};
        verify_removal(raw, target, result);

        target = 1;
        result = new Integer[] {0, 2, 3, 4, 5, 6};
        verify_removal(raw, target, result);

        target = 2;
        result = new Integer[] {0, 1, 3, 4, 5, 6};
        verify_removal(raw, target, result);

        target = 3;
        result = new Integer[] {0, 1, 2, 4, 5, 6};
        verify_removal(raw, target, result);

        target = 4;
        result = new Integer[] {0, 1, 2, 3, 5, 6};
        verify_removal(raw, target, result);

        target = 5;
        result = new Integer[] {0, 1, 2, 3, 4, 6};
        verify_removal(raw, target, result);

        target = 6;
        result = new Integer[] {0, 1, 2, 3, 4, 5};
        verify_removal(raw, target, result);
    }

    /**
     * Blackbox test for Solution.removeElements(..), focusing on input lists
     * of size 10000.
     */
    @Test(timeout=1000)
    public void large_lists() {
        //remove middle
        Integer[] raw = new Integer[10000];
        for(int i = 0; i < raw.length; i++) {
            raw[i] = i;
        }
        Integer[] result = new Integer[9999];
        for(int i = 0; i < 5000; i++) {
            result[i] = i;
        }
        for(int i = 5000; i < 9999; i++) {
            result[i] = i+1;
        }
        Integer target = 5000;
        verify_removal(raw, target, result);

        //remove front
        raw = new Integer[10000];
        for(int i = 0; i < raw.length; i++) {
            raw[i] = i;
        }
        result = new Integer[9999];
        for(int i = 0; i < 9999; i++) {
            result[i] = i+1;
        }
        target = 0;
        verify_removal(raw, target, result);

        //remove end
        raw = new Integer[10000];
        for(int i = 0; i < raw.length; i++) {
            raw[i] = i;
        }
        result = new Integer[9999];
        for(int i = 0; i < result.length; i++) {
            result[i] = i;
        }
        target = 9999;
        verify_removal(raw, target, result);
    }

    /**
     * Blackbox test for Solution.removeElements(..), focusing on input lists
     * of size ~10, with repeated elements.
     */
    @Test(timeout=1000)
    public void repeated_elements() {
        Integer[] result;
        Integer[] raw;
        Integer target;

        //list entirely composed of repeated targets (this test caught an issue)
        target = 0;
        raw = new Integer[] {0, 0};
        result = null;
        verify_removal(raw, target, result);

        //repeated non-targets present
        target = 0;
        raw = new Integer[] {2, 2, 0};
        result = new Integer[] {2, 2};
        verify_removal(raw, target, result);

        target = 0;
        raw = new Integer[] {0, 2, 2};
        result = new Integer[] {2, 2};
        verify_removal(raw, target, result);

        //repeated end targets
        target = 2;
        raw = new Integer[] {0, 2, 2};
        result = new Integer[] {0};
        verify_removal(raw, target, result);

        //repeated leading targets
        target = 2;
        raw = new Integer[] {2, 2, 0};
        result = new Integer[] {0};
        verify_removal(raw, target, result);

        target = 2;
        raw = new Integer[] {2, 2, 2, 2, 0};
        result = new Integer[] {0};
        verify_removal(raw, target, result);

        //repeated elements in the middle
        target = 1000;
        raw = new Integer[] {0, 1000, 1000, 1000, 0};
        result = new Integer[] {0, 0};
        verify_removal(raw, target, result);

        //non-contiguous repeated elements
        target = 1000;
        raw = new Integer[] {0, 1000, 1000, 1000, 0};
        result = new Integer[] {0, 0};
        verify_removal(raw, target, result);
    }
}





