public class Solution {

    public static int reverse(int j) {

        boolean negative = false;
        if(j<0){
            negative = true;
            j = -1*j;
        }

        String s = Integer.toString(j);
        String ns = "";

        for(int k = s.length()-1; k > -1; k--) {
            ns = ns + s.charAt(k);
        }

        System.out.println("original number: " + j);

        while(ns.charAt(0) == '0' && ns.length()>1) {
            ns = ns.substring(1);
        }

        System.out.println("reversed and trimmed string: " + ns);

        int answer = 0;
        for(int k = 0; k < ns.length(); k++) {
            Character c = ns.charAt(k);

            int i = Character.getNumericValue(c);
            int place = ns.length() - k - 1;
            double new_amount = i*Math.pow(10, place);

            try {
                Math.addExact(answer, (int) new_amount);
            } catch(ArithmeticException e) {
                System.out.println("there was overflow");
                return 0;
            }
        }

        if(negative) {
            answer = -1 * answer;
        }

        return answer;
    }

}
