import org.junit.Test;

public class testers {

    public static final int SECOND = 1000;

    @Test(timeout=SECOND)
    public void test1(){
        assert(2==2);
    }

    @Test(timeout=SECOND)
    public void test2(){
        Solution.reverse(-321);
    }
}
