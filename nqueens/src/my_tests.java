import org.junit.Test;
import org.junit.rules.Timeout;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static junit.framework.TestCase.fail;

public class my_tests {
    protected static final int SECOND = 1000;



    /**
     * An empty board is not added to answers
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

        Solution.fill_in(board, allowed, discovered_answers, n);

        System.out.println("board: " + board);
        System.out.println();
        System.out.println("allowed: " + allowed);
        System.out.println();
        System.out.println("answers: " + discovered_answers);
        System.out.println("-----------------------");
        assert discovered_answers.size() == 0;
    }

    /**
     * Confirm that fill_in adds a full board to answers
     */
    @Test(timeout=SECOND)
    public void baseCase1() {
        List<List<Integer>> actual_answers = new ArrayList<List<Integer>>();
        List<List<Integer>> discovered_answers = new ArrayList<List<Integer>>();
        ArrayList<Integer> board = new ArrayList<Integer>();
        ArrayList<Integer> allowed  = new ArrayList<Integer>();

        int n = 4;

        board.add(4);
        board.add(3);
        board.add(4);
        board.add(3);

        Solution.fill_in(board, allowed, discovered_answers, n);

        System.out.println("board: " + board);
        System.out.println();
        System.out.println("allowed: " + allowed);
        System.out.println();
        System.out.println("answers: " + discovered_answers);
        System.out.println("------------------------");
        assert discovered_answers.size() == 1;
    }

    /**
     * Confirm correct answer for board with 1 row left to fill
     * and only 1 more allowed column
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

        Solution.fill_in(board, allowed, discovered_answers, n);

        Solution.same_boards(discovered_answers, actual_answers);
    }

    /**
     * confirm that same_boards works
     */
    @Test(timeout=SECOND)
    public void test_same_boards(){
        List<List<Integer>> a = new ArrayList<List<Integer>>();
        List<List<Integer>> b = new ArrayList<List<Integer>>();

//        Create Lists to put in the 'boards' (lists) a and b
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

//        test same_boards when one of the lists has one list and the other is empty
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

}


