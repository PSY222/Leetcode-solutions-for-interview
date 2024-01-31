class Solution1 {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char,int> mg;
        for(char i:magazine)
            mg[i]++;

        for(char j:ransomNote){
            if(mg[j]>0){
                mg[j]--;
            }else{
                return false;
            }
        }         
        return true;
    }
};

class Solution2 {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> avail(26, 0);
        for (const auto & x: magazine) ++avail[x-'a'];
        for (const auto & x: ransomNote) if (avail[x-'a']-- == 0) return false;
        return true;
    }
};