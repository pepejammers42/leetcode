import java.util.HashMap;

public class leetcode1{
    public int[] twoSum(int[] nums, int target) {
        int [] r = new int[2];
        HashMap<Integer, Integer> hm = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            if (hm.containsKey(nums[i])){
                r[0] = hm.get(nums[i]);
                r[1] = i;
                break;
            }else{
                hm.put(target - nums[i], i);
            }
        }
        return r;
    }
}