public class Main {
    public static void main(String[] args) {
        String s = "main";
        System.out.println(s);
    }

    public static boolean isPalindrome(String s) {
        s = s.toLowerCase();
        boolean is = true; // assume true is problem for edge cases
        int a = 0;
        int b = s.length()-1;

        while(b>a) {
            if(s.charAt(a) != s.charAt(b)) {
                is = false;
                break;
            }
            a += 1;
            b -= 1;
            a = findAlphaNumericCharFront(a, s);
            b = findAlphaNumericCharBack(b, s);

        }
        return is;
    }

    private static int findAlphaNumericCharFront(int x, String s) {
        boolean aAlpha = Character.isLetter(s.charAt(x)) || Character.isDigit(s.charAt(x));

        while(!aAlpha)  {
            x += 1;
            aAlpha = Character.isLetter(s.charAt(x)) || Character.isDigit(s.charAt(x));
        }

        return x;
    }

    private static int findAlphaNumericCharBack(int x, String s) {
        boolean aAlpha = Character.isLetter(s.charAt(x)) || Character.isDigit(s.charAt(x));

        while(!aAlpha)  {
            x -= 1;
            aAlpha = Character.isLetter(s.charAt(x)) || Character.isDigit(s.charAt(x));
        }

        return x;
    }
}
