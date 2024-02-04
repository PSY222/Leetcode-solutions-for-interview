class Solution1 {
public:
    int count,ans;
    int kthSmallest(TreeNode* root, int k) {
        helper(root,k);
        return ans;
    }
    void helper(TreeNode* root, int k){
        if(root){
            kthSmallest(root->left,k);
            count++;
            if(count==k){
                ans=root->val;
            } 
            kthSmallest(root->right,k);
        }
        return;
    }
};

class Solution2 {
public:
    int kthSmallest(TreeNode* root, int k) {
        vector<int> v;
        inOrderTraversal(root,v);
        return v[k-1];
    }

    void inOrderTraversal(TreeNode* root, vector<int> &v){
        if(!root)    return;

        inOrderTraversal(root->left,v);
        v.push_back(root->val);
        inOrderTraversal(root->right, v);
    }
};