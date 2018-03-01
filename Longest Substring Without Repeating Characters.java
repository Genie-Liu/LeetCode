import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length() == 0) return 0;
        int maxLen = 0;
        int i = 0;
        int j = 0;
        HashMap<Character, Integer> hm = new HashMap<>();
        while(j < s.length()) {
            if(hm.containsKey(s.charAt(j))) {
                i = Math.max(i, hm.get(s.charAt(j)) + 1);
                hm.put(s.charAt(j), j);
            }else hm.put(s.charAt(j), j);
            maxLen = Math.max(j-i+1, maxLen);
            j++;
        }
        return maxLen;
    }
}