/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution1 {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        int carry = 0;

        while(l1 || l2 || carry != 0){
            int x = l1 ? l1->val: 0;
            int y = l2 ? l2->val : 0;
            int sum = carry + x+ y;
            carry = sum /10;
            curr->next = new ListNode(sum%10);
            curr = curr->next;
            l1 = l1 ? l1->next: nullptr;
            l2 = l2 ? l2->next: nullptr;
        }
        return dummy->next;        
    }
};

class Solution2{
    public: 
        ListNode* addTwoNumbers(ListNode* l1, ListNode* l2){
            return helper(l1,l2,0);
        }

    private:
        ListNode* helper(ListNode* n1, ListNode* n2, int carry){
            if(!n1 && !n2 && !carry){
                return  NULL;
            }

            int cur_sum = (n1 ? n1->val : 0) + (n2? n2->val : 0) + carry;
            ListNode* curr = new ListNode*cur_sum%10);
            curr-> next = helper(n1 ? n1->next : NULL, n2 ? n2->next : NULL, cur_sum//10);
            return curr;
        }
        
}