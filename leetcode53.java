// 53. Maximum Subarray

public class leetcode53 {
    public int maxSubArray(int[] nums) {
        int m = nums[0];
        int n = 0;
        
        for (int curr: nums){
            n = Math.max(curr, n + curr);
            m = n > m ? n: m;
        }
        return m;
    }    
}
