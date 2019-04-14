// a faster version is to use HashMap datastructure;
// exchange the time and space cost

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] rlt = new int[2];
        for(int i = 0; i < nums.length-1; i++) {
            for (int j = i+1; j < nums.length; j++) {
                if(nums[i] + nums[j] == target) {
                    rlt[0] = i;
                    rlt[1] = j;
                    return rlt;
                }
            }
        }
        return rlt;
    }
}