public class leetcode38 {
    
    public String countAndSay(int n) {
        String output = "1";
        String temp = "";
        char curr; 
        int prev = 0;
        for(int i = 1; i < n; i++){
            curr = output.charAt(0);
            for(int k = 0; k < output.length(); k++){
                if (output.charAt(k) != curr){
                    temp += String.valueOf((k-prev ==0)? 1: k-prev) + output.charAt(k-1);
                    prev = k;
                    curr = output.charAt(k);
                }
            }
            temp += String.valueOf(output.length()-prev) + output.charAt(prev);
            output = temp;
            temp = "";
            prev = 0;
        }
        
        return output;
        
    }
        
    public static void main(String[] args) {
        System.out.println(new leetcode38().countAndSay(7));       
    }
}

