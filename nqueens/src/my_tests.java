import org.junit.Test;
import org.junit.rules.Timeout;

import java.util.ArrayList;
import java.util.List;

public class my_tests {
    protected static final int SECOND = 1000;


    List<List<Integer>> answers = new ArrayList<List<Integer>>();
    ArrayList<Integer> board = new ArrayList<Integer>();
    ArrayList<Integer> allowed  = new ArrayList<Integer>();

    /**
     * An empty board is not added to answers
     */
    @Test(timeout=SECOND)
    public void baseCase() {
        int n = 4;

        board.add(4);
        board.add(3);

        Solution.fill_in(board, allowed, answers, n);

        System.out.println("board: " + board);
        System.out.println();
        System.out.println("allowed: " + allowed);
        System.out.println();
        System.out.println("answers: " + answers);
        System.out.println("-----------------------");
        assert answers.size() == 0;
    }

    /**
     * Confirm that fill_in adds a full board to answers
     */
    @Test(timeout=SECOND)
    public void baseCase1() {
        int n = 4;

        board.add(4);
        board.add(3);
        board.add(4);
        board.add(3);

        Solution.fill_in(board, allowed, answers, n);

        System.out.println("board: " + board);
        System.out.println();
        System.out.println("allowed: " + allowed);
        System.out.println();
        System.out.println("answers: " + answers);
        System.out.println("------------------------");
        assert answers.size() == 1;
    }
}


