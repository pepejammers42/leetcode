public class leetcode153 {
    public int findMin(int[] nums) {
        int res = nums[0];
        int l = 0;
        int r = nums.length - 1;
        
        while (l < r){
            int m = (l + r) / 2;
            if (nums[l] <= nums[m] && nums[m] <= nums[r])
                return nums[l];
            else if (nums[m] > nums[m + 1])
                return nums[m+1];
            else if (nums[m] < nums[m - 1])
                return nums[m];
            else if (nums[m] > nums[r])
                l = m + 1;
            else if (nums[m] < nums[r])
                r = m - 1;
        }
        return res;
    }   
}
