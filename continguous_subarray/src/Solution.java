public class Solution {

    /** find the largest continguous subarray of {@code nums} and
     * returns its sum.
     *
     * @param nums The array of interest
     * @return bigSum The sum of the largest contiguous subarray of {@code nums}
     */
    public static int maxSubArray(int[] nums) {
        int L = nums.length;
        int bigSum = nums[0];
        int bigStart = -1;
        int bigFinish = -1;

        for(int start = 0; start <= L-1; start++){
            int sum = 0;
            for(int last = start; last <= L - 1; last++) {
                sum += nums[last];
                if(sum > bigSum) {
                    bigSum = sum;
                    bigStart = start;
                    bigFinish = last;
                }
            }
        }

        return bigSum;
    }

    /**
     * Performs the same operation as maxSubArray, but is slower.
     * @param nums
     * @return bigSum
     */
    public static int maxSubArraySlow(int[] nums) {
//        System.out.println("maxSubArray: start");

        int L = nums.length;
        int bigSum = nums[0];
        int bigStart = -1;
        int bigNum = -1;

        for(int num = 1; num <= L; num++) {
//            System.out.println("SubArray Lenght: " + num);
            int final_start = L - num;
            for(int start = 0; start <= final_start; start++) {
//                System.out.println("   SubArray start: " + start);
                int sum = sumArray(start, start + num - 1, nums);
//                System.out.println("   SubArray sum: " + sum);
                if(sum > bigSum) {
                    bigSum = sum;
                    bigStart = start;
                    bigNum = num;
                }
            }
        }
//        System.out.println("array elements: " + nums[0]);
//        System.out.println("start of sequence: " +bigStart);
//        System.out.println("number of elements in: " + bigNum);

        return bigSum;
    }

    /**
     * Adds up all the elements in a subarray of {@code array} with initial index given by {@param initial}
     * and final index given by {@param finali}
     * @param initial
     * @param finali
     * @param array
     * @return
     */
    public static int sumArray(int initial, int finali, int[] array) {
        int sum = 0;
        for(int i = initial; i <= finali; i++) {
            sum += array[i];
        }
        return sum;
    }

}
