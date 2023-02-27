import java.util.*;

public class leetcode1832{
    public boolean checkIfPangram(String sentence) {
        if (sentence.length() < 26) return false;
        HashSet<Character> set = new HashSet<>();
        for(char ch: sentence.toCharArray()) {
            set.add(ch);
        }
        return set.size() == 26;
    }
    public static void main(String [] args){
       System.out.println(new leetcode1832().checkIfPangram("leetcode")); 
    }
}