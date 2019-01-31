import org.junit.Test;
import org.junit.rules.Timeout;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Vector;

import static junit.framework.TestCase.fail;

public class my_tests {
    protected static final int SECOND = 1000;

    /**
     * Whitebox test for fill_in(). Confirm that an empty board is not
     * considered a final answer. Restated, an empty List<Integer> is not
     * being added to the List<List<Integer>>.
     */
    @Test(timeout=SECOND)
    public void baseCase() {
        int n = 4;
        List<List<Integer>> actual_answers = new ArrayList<List<Integer>>();
        List<List<Integer>> discovered_answers = new ArrayList<List<Integer>>();
        ArrayList<Integer> board = new ArrayList<Integer>();
        ArrayList<Integer> allowed  = new ArrayList<Integer>();

        board.add(4);
        board.add(3);

        Solution.fill_in(board, allowed, discovered_answers, n, 0);

        System.out.println("board: " + board);
        System.out.println();
        System.out.println("allowed: " + allowed);
        System.out.println();
        System.out.println("resulting answers: " + discovered_answers);
        System.out.println("-----------------------");
        assert discovered_answers.size() == 0;

        Solution.same_boards(actual_answers, discovered_answers);
    }

    /**
     * Whitebox test for fill_in(). Confirm that fill_in considers a full board
     * as a final answer. Restated: A List<Integers> that is full (has n
     * elements) is added to List<List<Integer>>.
     */
    @Test(timeout=SECOND)
    public void baseCase1() {
        int n = 4;
        List<List<Integer>> actual_answers = new ArrayList<List<Integer>>();
        List<List<Integer>> discovered_answers = new ArrayList<List<Integer>>();
        ArrayList<Integer> allowed = new ArrayList<Integer>(Arrays.asList(new Integer[]{}));
        ArrayList<Integer> board = new ArrayList<Integer>(Arrays.asList(new Integer[]{4,3,4,3}));

        Solution.fill_in(board, allowed, discovered_answers, n, 0);

        System.out.println("board: " + board);
        System.out.println();
        System.out.println("allowed: " + allowed);
        System.out.println();
        System.out.println("answers: " + discovered_answers);
        System.out.println("------------------------");
        assert discovered_answers.size() == 1;
        actual_answers.add(Arrays.asList(new Integer[]{4,3,4,3}));

        Solution.same_boards(actual_answers, discovered_answers);
    }

    /**
     * Blackbox test for fill_in(..). When a board has one row left to fill, and
     * there is one allowed column left, fill_in(..) will assign that column,
     * thus filling the board. A List<Integers> ('board') with n-1 elements has
     * an element added to it when another List<Integers> ('allowed')
     * is not empty.
     */
    @Test(timeout=SECOND)
    public void recursiveCase() {
        int n = 4;
        List<List<Integer>> actual_answers = new ArrayList<List<Integer>>();
        List<List<Integer>> discovered_answers = new ArrayList<List<Integer>>();

        ArrayList<Integer> board = new ArrayList<Integer>(Arrays.asList(0,1,2));
        ArrayList<Integer> allowed = new ArrayList<Integer>(Arrays.asList(3));
        ArrayList<Integer> answer = new ArrayList<Integer>(Arrays.asList(0,1,2,3));
        actual_answers.add(answer);

        Solution.fill_in(board, allowed, discovered_answers, n, 0);
        Solution.same_boards(discovered_answers, actual_answers);
    }

    /**
     * Blackbox test for fill_in(..). Find the solutions to the 2x2 board,
     * where the queen is not allowed to move diagonally.
     */
    @Test(timeout=SECOND)
    public void recursiveCase2() {
        int n=2;
        List<List<Integer>> actual_answers = new ArrayList<List<Integer>>();
        List<List<Integer>> discovered_answers = new ArrayList<List<Integer>>();

        ArrayList<Integer> board = new ArrayList<Integer>(Arrays.asList());
        ArrayList<Integer> allowed = new ArrayList<Integer>(Arrays.asList(0,1));
        ArrayList<Integer> answer1 = new ArrayList<Integer>(Arrays.asList(0,1));
        ArrayList<Integer> answer2 = new ArrayList<Integer>(Arrays.asList(1,0));
        actual_answers.add(answer1);
        actual_answers.add(answer2);

        Solution.fill_in(board, allowed, discovered_answers, n, 0);
        Solution.same_boards(discovered_answers, actual_answers);
    }

    /**
     * Blackbox test for fill_in(..). Find the solutions to the 3x4 board,
     * where the queen is not allowed to move diagonally.
     */
    @Test(timeout=SECOND)
    public void recursiveCase3() {
        int n=3;
        List<List<Integer>> actual_answers = new ArrayList<List<Integer>>();
        List<List<Integer>> discovered_answers = new ArrayList<List<Integer>>();

        ArrayList<Integer> board = new ArrayList<Integer>(Arrays.asList());
        ArrayList<Integer> allowed = new ArrayList<Integer>(Arrays.asList(0,1,2));
        ArrayList<Integer> answer1 = new ArrayList<Integer>(Arrays.asList(0,1,2));
        ArrayList<Integer> answer2 = new ArrayList<Integer>(Arrays.asList(0,2,1));
        ArrayList<Integer> answer3 = new ArrayList<Integer>(Arrays.asList(1,0,2));
        ArrayList<Integer> answer4 = new ArrayList<Integer>(Arrays.asList(1,2,0));
        ArrayList<Integer> answer5 = new ArrayList<Integer>(Arrays.asList(2,0,1));
        ArrayList<Integer> answer6 = new ArrayList<Integer>(Arrays.asList(2,1,0));

        actual_answers.add(answer1);
        actual_answers.add(answer2);
        actual_answers.add(answer3);
        actual_answers.add(answer4);
        actual_answers.add(answer5);
        actual_answers.add(answer6);

        Solution.fill_in(board, allowed, discovered_answers, n, 0);
        Solution.same_boards(discovered_answers, actual_answers);
    }

    /**
     * Blackbox test for same_boards. When handed two identical sets of answers
     * (List<List<Integer>>, same_boards does not throw an error. If the two
     * sets of answers are different, same_boards throws an error. Note: order
     * of the answers matters.
     */
    @Test(timeout=SECOND)
    public void test_same_boards(){
//        create two boards
        List<List<Integer>> a = new ArrayList<List<Integer>>();
        List<List<Integer>> b = new ArrayList<List<Integer>>();
//        Create Lists to put in the 'boards'
        List<Integer> one = new ArrayList<>();
        one.add(4);
        one.add(5);
        List<Integer> two = new ArrayList<>();
        for(int k = 0; k < 3000; k++){
            two.add(k);
        }
        List<Integer> three = new ArrayList<>();

//       test same_boards on two empty lists
        Solution.same_boards(a, b);

//        test same_boards when one of the boards has one list and the other is empty
        a.add(one);
        try {
            Solution.same_boards(a,b);
            fail("error should have been thrown");
        } catch (AssertionError e) {
        }

//        both lists contain the same list
        b.add(one);
        Solution.same_boards(a,b);

//        both lists contain two lists, though one of those contained lists is different
        a.add(two);
        b.add(three);
        try {
            Solution.same_boards(a,b);
            fail("error should have been thrown");
        } catch (AssertionError e) {
        }

//        the lists are identical, each holding a list with 2 ints, a lists with 3000 ints, and a list
//        with no ints
        a.remove(two);
        a.add(three);
        a.add(two);
        b.add(two);
        Solution.same_boards(a,b);
    }

    /**
     * whitebox test for fill_in_final(..). Confirm that a board of the
     * appropriate size is added to answers, regardless of whether or not
     * allowed is empty.
     */
    @Test(timeout=SECOND)
    public void base_case_final(){
        int n = 4;
        List<List<Integer>> actual_answers = new ArrayList<List<Integer>>();
        List<List<Integer>> discovered_answers = new ArrayList<List<Integer>>();
        ArrayList<Integer> board = new ArrayList<Integer>(Arrays.asList(3,2,1,0));
        ArrayList<Integer> allowed  = new ArrayList<Integer>(Arrays.asList(4,3,2,9));

        ArrayList<Integer> answer1 = new ArrayList<Integer>(Arrays.asList(3, 2, 1, 0));
        actual_answers.add(answer1);

        Solution.fill_in_final(board, allowed, discovered_answers, n, 0);

        Solution.same_boards(discovered_answers, actual_answers);
    }

    /**
     * Blackbox test for base_case_final(..) for the n=4 case.
     */
    @Test(timeout=SECOND)
    public void n4_final() {
        int n = 4;
        List<List<Integer>> actual_answers = new ArrayList<List<Integer>>();
        List<List<Integer>> discovered_answers = new ArrayList<List<Integer>>();
        ArrayList<Integer> board = new ArrayList<Integer>(Arrays.asList());
        ArrayList<Integer> allowed  =
                new ArrayList<Integer>(Arrays.asList(0, 1, 2, 3));

        ArrayList<Integer> answer1 =
                new ArrayList<Integer>(Arrays.asList(1, 3, 0, 2));
        ArrayList<Integer> answer2 =
                new ArrayList<Integer>(Arrays.asList(2, 0, 3, 1));

        actual_answers.add(answer1);
        actual_answers.add(answer2);

        Solution.fill_in_final(board,
                allowed, discovered_answers, 4, 0);

        Solution.same_boards(actual_answers, discovered_answers);
    }

    @Test(timeout=SECOND)
    public void test_vector(){
        Vector<String> v = new Vector<String>();
        v.add("sugar");
        v.add("salt");
        System.out.println(v.capacity());
        System.out.println(v.size());
    }

    @Test(timeout=SECOND)
    public void convert() {
        int n = 4;

        List<List<String>> v = Solution.solveNQueens(n);

        System.out.println(v.size());
        System.out.println(v.get(0));
        System.out.println(v.get(1));

    }
}


