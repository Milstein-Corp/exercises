import java.util.ArrayList;
import java.util.Arrays;

import java.util.Iterator;
import java.util.List;

public class Solution {

    public static List<List<String>> solveNQueens(int n) {

        ArrayList<String> answer;
        List<List<String>> answers = new ArrayList<List<String>>();

        for(int i = 0; i < 2; i++) {


            answer = new ArrayList<String>();
            for (int r = 0; r < n; r++) {
                String row = "";
                for (int c = 0; c < n; c++) {
                    row += ".";
                }
                answer.add(row);
            }
            answers.add(answer);



        }

        return answers;
    }

    public static void fill_in(ArrayList<Integer> board,
                               ArrayList<Integer> allowed,
                               List<List<Integer>> answers, int n) {

        if(board.size() == n) { // the board is full of queens
            answers.add(board);

        } else { //iterate over all the remaining allowed values
            for (Iterator<Integer> it = allowed.iterator(); it.hasNext(); ) {
                int a = it.next();
                board.add(a);
                allowed.remove(Integer.valueOf(a));
                fill_in(board, allowed, answers, n);
                board.remove(board.size());
                allowed.add(Integer.valueOf(a));
            }
        }
    }

    public static void same_boards(List<List<Integer>> discovered_answers,
                                   List<List<Integer>> actual_answers) {
        assert discovered_answers.size() == actual_answers.size();

        for(int i = 0; i < discovered_answers.size(); i++) {
            List<Integer> d = discovered_answers.get(i);
            List<Integer> a = actual_answers.get(i);
            assert d.size() == a.size();
            for(int j = 0; j < d.size(); j++) {
                assert d.get(j) == a.get(j);
            }
        }

    }
}
