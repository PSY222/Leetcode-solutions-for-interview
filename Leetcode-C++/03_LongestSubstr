class Solution1{
    public:
        int lengthOfLongestSubString(string s){
            int n = s.length();
            int maxLength = 0;
            unordered_set<char> charSet;
            int left = 0;

            for(int right = 0; right <n; right++){
                if(charSet.count(s[right])==0){
                    charSet.insert(s[right]);
                    maxLength = max(maxLength, right-left+1);
                }else{
                    while(charSet.count(s[right])){
                        charSet.erase(s[left]);
                        left++;
                    }
                    charSet.insert(s[right]);
                }
            }
            return maxLength;
        }
};

class Solution2{
    public:
        int lengthOfLongestSubString(string s){
            int n = s.length();
            int maxLength = 0;
            unordered_map<char,int> charMap;
            int left = 0;

            for (int right = 0; right <n; right++){
                if(charMap.count(s[right])==0 || charMap[s[right]] < left){
                    charMap[s[right]] = right;
                    maxLength = max(maxLength, right-left +1);
                }else{
                    left = charMap[s[right]]+1;
                    charMap[s[right]]=right;
                }
            }
            return maxLength;
        }
};


class Solution3{
    public: 
        int lengthOfLongestSubString(string s){
            int store[256] = {0};
            int l=0;
            int r=0;
            int ans = 0;

            while(r<s.length())
            {
                store[s[r]]++;
                while(store[s[r]>1]){
                    store[s[l]]--;
                    l++;
                }
                ans = max(ans,r-l+1);
                r++;
            }
            return ans;
        }
};