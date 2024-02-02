#include <vector>
#include <algorithm>

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        deque<vector<int>> merged;
        sort(intervals.begin(), intervals.end());
        merged.push_back(intervals[0]);

        for(size_t i=1; i<intervals.size(); ++i){
            int currStart = intervals[i][0];
            int currEnd = intervals[i][1];
            int mergedEnd = merged.back()[1];
            int mergedStart = merged.back()[0];

            if(currStart <= mergedEnd){
                merged.back()[1] = max(currEnd, mergedEnd);
            }else{
                merged.push_back(intervals[i]);
            }
        }
        return vector<vector<int>>(merged.begin(),merged.end());
    }
};