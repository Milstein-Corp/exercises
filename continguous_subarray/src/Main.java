public class Main {

    public static void main(String[] args) {
        int[] s = new int[]{-2,1,-3,4,-1,2,1,-5,4};
        int largest = Solution.maxSubArray(s);
        System.out.println("maxSubArray: " + largest);
    }
}
