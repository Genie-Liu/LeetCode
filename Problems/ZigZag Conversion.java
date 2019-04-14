import java.util.ArrayList;

class Solution {
    public String convert(String s, int numRows) {
        ArrayList<ArrayList<Character>> store = new ArrayList<>();
        if(numRows == 1) return s;
        for(int i = 0; i < numRows; i++){
            store.add(new ArrayList<>());
        }
        int m = 2*numRows-2;
        for(int i = 0; i < s.length(); i++) {
            int p = i % m;
            if(p > numRows-1) p = 2*(numRows-1)-p;
            store.get(p).add(s.charAt(i));
        }
        for(int i = 1; i < numRows; i++) {
            store.get(0).addAll(store.get(i));
        }
        char[] cc = new char[s.length()];
        for(int i = 0; i < s.length(); i++) {
            cc[i] = store.get(0).get(i);
        }
        return String.valueOf(cc);
    }
}