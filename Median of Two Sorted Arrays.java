class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        double maxleft, minright;

        if(m > n) {
            int tmp = m;
            m = n;
            n = tmp;

            int[] tmp = nums1;
            nums1 = nums2;
            nums2 = tmp;
        }

        int imin = 0;
        int imax = m;
        int i = (imin+imax)/2;
        int j = (m+n+1)/2-i;
        while(true) {
            if((i==0 || j == n || nums1[i-1] <= nums2[j]) && (i == m || j == 0 || nums1[i] >= nums2[j-1])) break;
            else if(j != 0 && nums1[i] < nums2[j-1] && i != m){
                i++;
                j = (m+n+1)/2-i;
            }
            else {
                i--;
                j = (m+n+1)/2-i;
            }
        }
        if(i == 0) maxleft = nums2[j-1];
        else if(j == 0) maxleft = nums1[i-1];
        else maxleft = Math.max(nums1[i-1], nums2[j-1]);

        if((m+n) % 2 == 1) return maxleft;

        if(i == m) minright = nums2[j];
        else if(j == n) minright = nums1[i];
        else minright = Math.min(nums1[i], nums2[j]);

        return (maxleft+minright)/2;
    }
}