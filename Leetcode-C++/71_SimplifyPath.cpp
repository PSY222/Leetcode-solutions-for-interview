class Solution {
public:
    string simplifyPath(string path) {
        stack<string> st;
        string res;
        string temp;
        
        for(int i = 0;  i<path.size(); ++i)
        {
            if(path[i] == '/')    
                continue;
            temp.clear();
            while(i < path.size() && path[i] != '/')
            {
                temp += path[i++];
            }
            if(temp == ".")
                continue;
            else if(temp == "..")
            {
                if(!st.empty())
                    st.pop();
            }
            else
                st.push(temp);
        }
        
        while(!st.empty())
        {
            res = "/" + st.top() + res;
            st.pop();
        }
        
        return res.size()==0 ? "/" : res;
    }
};