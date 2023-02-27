import java.util.HashMap;
import java.util.Map;

public class leetcode219{
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> hm = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            if (hm.containsKey(nums[i]) && i - hm.get(nums[i]) <= k)
                return true;
            hm.put(nums[i], i);
        }
        return false;        
    }
    
    public static void main(String[] args) {
        int [] test = {1,0,1,1};
        System.out.println(new leetcode219().containsNearbyDuplicate(test, 1));
    }
}
