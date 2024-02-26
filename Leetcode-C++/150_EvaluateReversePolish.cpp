class Solution1 {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        unordered_map<string,function<int(int,int)>> map{
            {"+", plus<int>()},
            {"-",minus<int>()},
            {"*",multiplies<int>()},
            {"/",divides<int>()}
        };

        for(const auto& t: tokens){
            const auto& op = map.find(t);
            if(op != map.end()){
                assert(s.size() >= 2);
                int right = s.top(); s.pop();
                int left = s.top(); s.pop();
                s.push((*op).second(left,right));
            } else{
                s.push(stoi(t));
            }
        }
        return s.top();
    }
};

class Solution2 {
public:
    stack<int> st;
    void operation(string& op){
        if(st.empty()) return;
        int n2 = st.top();
        st.pop();

        if(st.empty()) return;
        int n1 = st.top();
        st.pop();

        int x = 0;
        switch(op[0]){
            case '+' : x = n1 + n2; break;
            case '-' : x = n1 - n2; break;
            case '*' : x = n1 * n2; break;
            case '/' : x = n1 / n2; break;
        }
        st.push(x);
    }
    int evalRPN(vector<string>& tokens) {
        int ans = 0;
        for(string& s : tokens){
            if(s == "+" || s == "-" || s == "/" || s == "*"){
                operation(s);
            }
            else{
                ans = stoi(s);
                st.push(ans);
            }
        }
        if(st.empty()) return 0;
        return st.top();
    }
};