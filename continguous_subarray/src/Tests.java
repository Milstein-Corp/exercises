import org.junit.Test;

public class Tests {
    protected static final int SECOND = 1000;
    /**The problem: find the contiguous subarray with the largest sum,
     *and return that sum.
     *if array = [-2,1,-3,4,-1,2,1,-5,4], answer is 6.
     *explanation: [4, -1, 2, 1]
     */
    @Test(timeout=SECOND)
    public void problem() {
        int[] s = new int[]{-2,1,-3,4,-1,2,1,-5,4};
        int answer = Solution.maxSubArray(s);
        assert answer == 6;
    }

    @Test(timeout=SECOND)
    public void edgeCase() {
        int[] s = new int[]{-2};
        int answer = Solution.maxSubArray(s);
        assert answer == -2;

        s = new int[]{-2, 8};
        answer = Solution.maxSubArray(s);
        assert answer == 8;
    }

    //test helper method
    @Test(timeout=SECOND)
    public void testArraySum(){
        int[] s = new int[]{-2,1,-3,4,-1,2,1,-5,4};
        int sum = Solution.sumArray(0,3,s);
        assert sum == 0;

        sum = Solution.sumArray(1,3,s);
        assert sum == 2;

        sum = Solution.sumArray(4,8,s);
        assert sum == 1;
    }
}
