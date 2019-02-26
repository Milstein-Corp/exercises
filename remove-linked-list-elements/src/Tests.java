import org.junit.Test;
import src.Solution.ListNode;
import src.Solution;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;

import static junit.framework.TestCase.fail;

public class Tests {
    ListNode example;

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
    public void first(){

        ListNode l = dummy_list();
        print_ll(l);
        System.out.println("****************");

        ListNode head = Solution.removeElements(l, 1);

        print_ll(head);

    }
}
