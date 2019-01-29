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
                               List<List<Integer>> answers, int n, int depth) {

        if(board.size() == n) { // the board is full of queens
            System.out.println(depth + ": base case");
            System.out.println("" + depth + ": " + "allowed = " + allowed);
            System.out.println("" + depth + ": " + "board = " + board);


            answers.add(List.copyOf(board));
            System.out.println("" + depth + ": " + "answers = " + answers);
            System.out.println();
        } else { //iterate over all the remaining allowed values
            int size = allowed.size();
            for (int it = 0; it < size; it++) {
                System.out.println(depth + ": recursive case");
                System.out.println("" + depth + ": " + "allowed = " + allowed);
                System.out.println("" + depth + ": " + "board = " + board);
                System.out.println("" + depth + ": " + "answers = " + answers);
                System.out.println("" + depth + ": " + "index = " + it);
                System.out.println();

                int a = allowed.remove(it);
                board.add(a);
                fill_in(board, allowed, answers, n, depth+1);

                board.remove(board.size()-1);
                allowed.add(it,a);
            }
        }
    }

    public static void fill_in_final(ArrayList<Integer> board,
                               ArrayList<Integer> allowed,
                               List<List<Integer>> answers, int n, int depth) {

        if(board.size() == n) { // the board is full of queens
            System.out.println(depth + ": base cases");
            System.out.println("" + depth + ": " + "allowed = " + allowed);
            System.out.println("" + depth + ": " + "board = " + board);


            answers.add(List.copyOf(board));
            System.out.println("" + depth + ": " + "answers = " + answers);
            System.out.println();
        } else { //iterate over all the remaining allowed values
            int size = allowed.size();
            for (int it = 0; it < size; it++) {
                System.out.println(depth + ": recursive case");
                System.out.println("" + depth + ": " + "allowed = " + allowed);
                System.out.println("" + depth + ": " + "board = " + board);
                System.out.println("" + depth + ": " + "answers = " + answers);
                System.out.println("" + depth + ": " + "index = " + it);
                System.out.println();

                int candiate = allowed.remove(it);
                int next_row = board.size();
                ArrayList<Integer> forbidden = new ArrayList<Integer>();
                for(int row = 0; row < next_row; row++) {
                    int occupied = board.get(row);
                    forbidden.add(occupied + next_row - row);
                    forbidden.add(occupied - row + next_row);
                }

                if(!forbidden.contains(candiate)){
                    board.add(next_row, candiate);
                    fill_in_final(board, allowed, answers, n, depth + 1);

                    board.remove(board.size() - 1);
                    allowed.add(it, candiate);
                } else {
                    allowed.add(it, candiate);
                }
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
