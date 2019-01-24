import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        List<List<String>> results = Solution.solveNQueens(8);

        for (Iterator<List<String>> it = results.iterator(); it.hasNext(); ) {
            ArrayList<String> board = (ArrayList<String>) it.next();
            System.out.println(board);
        }
    }
}
