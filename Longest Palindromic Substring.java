class Solution {
    public String longestPalindrome(String s) {
        String maxString = new String();
        int i;
        int j;
        int maxl=0;
        int len = s.length();
        // if(len==1) return s;
        for(int k = 0; k < len; k++) {
            if((k+1)*2 <= maxl || (len-k)*2 <= maxl) continue;
            if(k < len-1 && s.charAt(k) == s.charAt(k+1)) {
                i = k-1;
                j = k+2;
                while(i >= 0 && j < len && s.charAt(i) == s.charAt(j)) {
                    i--;
                    j++;
                }
                i++;
                j--;
                if(j-i+1 > maxl){
                    maxl = j-i+1;
                    maxString = s.substring(i, j+1);
                }
            }
            i = j = k;
            while(i >= 0 && j < len && s.charAt(i) == s.charAt(j)) {
                i--;
                j++;

            }
            i++;
            j--;
            if(j-i+1 > maxl){
                maxl = j-i+1;
                maxString = s.substring(i, j+1);
            }
        }
        return maxString;
    }
}