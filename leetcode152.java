// 152. Maximum Product Subarray

public class leetcode152 {
    public int maxProduct(int[] nums) {
       int gm = nums[0];
        int lm = 1;
        int ln = 1;
        
        for (int i = 0; i < nums.length; i++){
            int prev = lm; 
            lm = Math.max(nums[i], Math.max(lm * nums[i], ln * nums[i]));
            ln = Math.min(nums[i], Math.min(ln * nums[i], prev * nums[i]));
            System.out.println(lm + " "+ ln);
            
            gm = (lm > gm)? lm : gm;
        }
        return gm;
    }
    public static void main(String[] args) {
        int [] test = {-1, -2, -3, -4};
        System.out.println(new leetcode152().maxProduct(test));
    }
}
