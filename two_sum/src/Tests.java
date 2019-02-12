//make sure to import the annotation that you want
import org.junit.Test;



public class Tests {

    //annotation
    //barest bones signature that you can write
    @Test(timeout=1000)
    public void test1(){
        int[] nums = new int[]{2, 11, 7, 15};
        int target = 9;
        int[] discovered_ans = Solution.myTwoSum(nums, target);
        int[] actual_ans = new int[]{0, 2};

        Solution.same_arrays(discovered_ans,actual_ans);
    }

    @Test(timeout=1000)
    public void test2(){
        assert(1==1);
    }

}
