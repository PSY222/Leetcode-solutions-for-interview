class Solution {
public:
    bool isAnagram(string s, string t) {
        int n = s.length();
        if(n != t.length()) return false;
        unordered_map<char,int> cnt;
        for(int i = 0 ; i < n ; i++){
            cnt[s[i]]++;
            cnt[t[i]]--;
        }

        for(auto c:cnt)
            if(c.second) return false;
        return true;
    }
};