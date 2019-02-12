import java.util.HashMap;
import java.util.Map;

import static junit.framework.TestCase.fail;

class Solution {

    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        Map<Integer, Integer> map = new HashMap();
        for(int i=0; i<nums.length; i++){
            if(map.containsKey(target-nums[i])){
                int index = map.get(target-nums[i]);
                if(index != i){
                    result[1] = i;
                    result[0] = index;
                    break;
                }
            }
            map.put(nums[i], i);
        }
        return result;
    }

    public static int[] myTwoSum(int[] nums, int target) {
        for(int i = 0; i < nums.length; i++) {
            for(int j = i+1; j < nums.length; j++) {
                if(nums[i] + nums[j] == target) {
                    return new int[]{i,j};
                }
            }
        }
        return new int[]{-1,-1};
    }

    public static void same_arrays(int[] a, int[] b) {
        for(int i = 0; i < a.length; i++) {
            try {
                assert(a[i]==b[i]);
            } catch(Exception e) {
                fail("The second array was too small");
            }
        }
        for(int i = 0; i < b.length; i++) {
            try {
                assert(a[i]==b[i]);
            } catch(Exception e) {
                fail("The first array was too small");
            }
        }
    }

}
