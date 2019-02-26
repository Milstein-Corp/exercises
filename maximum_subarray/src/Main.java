public class Main {

    /**
     * Demonstrates Solution.maxSubArray(int[] s)
     * See problem() in Tests.java for example
     * @param args
     */
    public static void main(String[] args) {
        int[] s = new int[]{-2,1,-3,4,-1,2,1,-5,4};
        int largest = Solution.maxSubArray(s);
        System.out.println("maxSubArray: " + largest);
    }
}
