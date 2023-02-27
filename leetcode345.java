import java.util.*;

public class leetcode345 {
    public String reverseVowels(String s) {
        List<Character> vowels = new ArrayList<Character>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        
        StringBuilder sb = new StringBuilder();
        StringBuilder v = new StringBuilder(); 
        Deque<Character> dq = new LinkedList<Character>();
            for (char c : s.toCharArray()){
                if (vowels.contains(c))
                    dq.add(c);
                else
                    sb.append(c);
            } 
            
        return sb.toString();
    } 
    public static void main(String[] args) {
        
    }
}
