import org.junit.Test;
import src.Solution.ListNode;
import src.Solution;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

import static junit.framework.TestCase.fail;

public class Tests {
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

    public ListNode linked_list(Integer[] a) {
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

    public void print_ll(ListNode l) {
        while(l != null) {
            System.out.println(l.val);
            l = l.next;
        }
    }

    public void lists_match(ListNode l1, ListNode l2) {
        while(l1 != null && l2 != null) {
            assert(l1.val == l2.val);
            l1 = l1.next;
            l2 =l2.next;
        }
        assert(l1 == null && l2 == null); 
    }

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

    @Test(timeout=1000)
    public void small_lists() {
        //empty initial list
        ListNode initial = null;
        ListNode head = Solution.removeElements(initial, 0);
        ListNode correct_answer = null;
        lists_match(head, correct_answer);

        //size=1, remove it
        initial = linked_list(
                new Integer[] {0});
        head = Solution.removeElements(initial, 0);
        correct_answer = null;
        lists_match(head, correct_answer);

        //size=1, leave it
        initial = linked_list(
                new Integer[] {0});
        head = Solution.removeElements(initial, 5);
        correct_answer = linked_list(
                new Integer[] {0});
        lists_match(head, correct_answer);

        //size=2, remove nothing
        initial = linked_list(
                new Integer[] {0, 2});
        head = Solution.removeElements(initial, 5);
        correct_answer = linked_list(
                new Integer[] {0, 2});
        lists_match(head, correct_answer);

        //size=2, remove leading element
        initial = linked_list(
                new Integer[] {0, 2});
        head = Solution.removeElements(initial, 0);
        correct_answer = linked_list(
                new Integer[] {2});
        lists_match(head, correct_answer);

        //size=2, remove trailing element
        initial = linked_list(
                new Integer[] {0, 2});
        head = Solution.removeElements(initial, 2);
        correct_answer = linked_list(
                new Integer[] {0});
        lists_match(head, correct_answer);
    }

    @Test(timeout=1000)
    public void reg_lists() {

        Integer[] raw = new Integer[] {0, 1, 2, 3, 4, 5, 6};
        Integer target = 0;
        Integer[] result = new Integer[] {1, 2, 3, 4, 5, 6};
        verify_removal(raw, target, result);

        ListNode initial = linked_list(
                new Integer[] {0, 1, 2, 3, 4, 5, 6});
        ListNode head = Solution.removeElements(initial, 6);
        ListNode correct_answer = linked_list(
                new Integer[] {0, 1, 2, 3, 4, 5});
        lists_match(head, correct_answer);

        initial = linked_list(
                new Integer[] {0, 1, 2, 3, 4, 5, 6});
        head = Solution.removeElements(initial, 3);
        correct_answer = linked_list(
                new Integer[] {0, 1, 2, 4, 5, 6});
        lists_match(head, correct_answer);

        initial = linked_list(
                new Integer[] {0, 1, 2, 3, 4, 5, 6});
        head = Solution.removeElements(initial, 1);
        correct_answer = linked_list(
                new Integer[] {0, 2, 3, 4, 5, 6});
        lists_match(head, correct_answer);

        initial = linked_list(
                new Integer[] {0, 1, 2, 3, 4, 5, 6});
        head = Solution.removeElements(initial, 5);
        correct_answer = linked_list(
                new Integer[] {0, 1, 2, 3, 4, 6});
        lists_match(head, correct_answer);
    }

    private void verify_removal(Integer[] raw, Integer target,Integer[] desired_result) {
        ListNode raw_ll = linked_list(raw);
        ListNode result = Solution.removeElements(raw_ll, target);
        ListNode desired_result_ll = linked_list(desired_result);
        lists_match(result, desired_result_ll);
    }

    @Test(timeout=1000)
    public void large_lists() {

        //remove middle
        Integer[] a = new Integer[10000];
        for(int i = 0; i < a.length; i++) {
            a[i] = i;
        }
        ListNode initial = linked_list(a);
        ListNode head = Solution.removeElements(initial, 5000);
        Integer[] b = new Integer[9999];
        for(int i = 0; i < 5000; i++) {
            b[i] = i;
        }
        for(int i = 5000; i < 9999; i++) {
            b[i] = i+1;
        }
        ListNode correct_answer = linked_list(b);
        lists_match(head, correct_answer);

        //remove front
        a = new Integer[10000];
        for(int i = 0; i < a.length; i++) {
            a[i] = i;
        }
        initial = linked_list(a);
        head = Solution.removeElements(initial, 0);
        b = new Integer[9999];
        for(int i = 0; i < 9999; i++) {
            b[i] = i+1;
        }
        correct_answer = linked_list(b);
        lists_match(head, correct_answer);

        //remove end
        a = new Integer[10000];
        for(int i = 0; i < a.length; i++) {
            a[i] = i;
        }
        initial = linked_list(a);
        head = Solution.removeElements(initial, 9999);
        b = new Integer[9999];
        for(int i = 0; i < b.length; i++) {
            b[i] = i;
        }
        correct_answer = linked_list(b);
        lists_match(head, correct_answer);
    }

    @Test(timeout=1000)
    public void repeated_elements_small() {
        //list entirely composed of repeated elements (this test caught an issue)
        ListNode initial = linked_list(
                new Integer[] {0, 0});
        ListNode head = Solution.removeElements(initial, 0);
        ListNode correct_answer = null;
        lists_match(head, correct_answer);

        //repeated non-target elements
        initial = linked_list(
                new Integer[] {0, 0});
        head = Solution.removeElements(initial, 5);
        correct_answer = linked_list(
                new Integer[] {0, 0});
        lists_match(head, correct_answer);

        //repeated end elements
        initial = linked_list(
                new Integer[] {0, 2, 2});
        head = Solution.removeElements(initial, 2);
        correct_answer = linked_list(
                new Integer[] {0});
        lists_match(head, correct_answer);

        //repeated leading elements
        initial = linked_list(
                new Integer[] {2, 2, 0});
        head = Solution.removeElements(initial, 2);
        correct_answer = linked_list(
                new Integer[] {0});
        lists_match(head, correct_answer);

        //repeated elements in the middle
        initial = linked_list(
                new Integer[] {0, 2, 2, 0});
        head = Solution.removeElements(initial, 2);
        correct_answer = linked_list(
                new Integer[] {0, 0});
        lists_match(head, correct_answer);

        //non contiguous repeated elements
        initial = linked_list(
                new Integer[] {2, 0, 0, 0});
        head = Solution.removeElements(initial, 2);
        correct_answer = linked_list(
                new Integer[] {0, 0, 0});
        lists_match(head, correct_answer);
    }

    @Test(timeout=1000)
    public void repeated_elements_reg() {

    }

    @Test(timeout=1000)
    public void repeated_elements_large() {

    }

}





