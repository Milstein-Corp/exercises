public class Main {
    public static void main(String[] args) {
        String s = "main";
        System.out.println(s);
    }

    public static boolean isPalindrome(String s) {
        if(s.isEmpty()) {
            return true;
        }
        s = s.toLowerCase();
        boolean is = true; // assume true is problem for edge cases
        int a = 0;
        int b = s.length()-1;

        int[] pos = findAlphaNumericChar(a, b, s);
        a = pos[0];
        b = pos[1];

        while(b>a) {
            if(s.charAt(a) != s.charAt(b)) {
                is = false;
                break;
            }
            a += 1;
            b -= 1;
            pos = findAlphaNumericChar(a, b, s);
            a = pos[0];
            b = pos[1];
        }
        return is;
    }

    private static int[] findAlphaNumericChar(int a, int b, String s) {
        boolean aAlpha = Character.isLetter(s.charAt(a)) || Character.isDigit(s.charAt(a));
        boolean bAlpha = Character.isLetter(s.charAt(b)) || Character.isDigit(s.charAt(b));

        while(!aAlpha && b>a)  {
            a += 1;
            aAlpha = Character.isLetter(s.charAt(a)) || Character.isDigit(s.charAt(a));
        }
        while(!bAlpha && b>a)  {
            b -= 1;
            bAlpha = Character.isLetter(s.charAt(b)) || Character.isDigit(s.charAt(b));
        }

        return new int[]{a, b};
    }
}
