// 1544. Make The String Great
public class leetcode1544{
    public String makeGood(String s) {
        if (s.length() < 2)
            return s;
        StringBuilder sb = new StringBuilder();

        for (char c: s.toCharArray()){
            if (!sb.isEmpty() && (sb.charAt(sb.length() - 1) ^ c) == 32)
                sb.deleteCharAt(sb.length()-1);
            else
                sb.append(c);
        }
        return sb.toString();
    }
}
