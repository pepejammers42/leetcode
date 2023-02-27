// 1323. Maximum 69 Number

public class leetcode1323 {
    public int maximum69Number (int num) {
        char [] conv = Integer.toString(num).toCharArray();
        
        for (int i = 0; i < conv.length; i++){
            if (conv[i] == '6'){
                conv[i] = '9'; 
                break;
            }
        }
        
        return Integer.valueOf(String.valueOf(conv));
    }   
}
