# class Solution:
#     def splitIntoFibonacci(self, num: str) -> List[int]:
#         if len(num) <=2:
#             return []

#         length =1
#         res = []
#         compare = ''
#         for i in range(1,len(num)-2):
#             if num[i] == '0':
#              continue
#             self.find(num,i,length,res)
#         return res
    
#     def find(self,num,i,length,res):
#         if i+length >= len(num)-1:
#             return
#         first = int(num[:i])
#         second = int(num[i:i+length])
#         third = int(num[i+length:])
#         if third ==  first + second :
#             res.extend([first, second, third]) 
#         else:
#             self.find(num,i,length+1,res)    


#java code source: https://leetcode.com/problems/split-array-into-fibonacci-sequence/solutions/139690/logical-thinking-with-clear-java-code/?orderBy=most_votes
public List<Integer> splitIntoFibonacci(String S) {
        List<Integer> result = new ArrayList<>();
        splitIntoFibonacciFrom(0, result, S); // start state
        return result;
    }

    private boolean splitIntoFibonacciFrom(int curIdx, List<Integer> result, String S) {
        if (curIdx == S.length() && result.size() >= 3) { // end state (base cases)
            return true;
        }
        for (int i = curIdx; i <= S.length() - 1; i++) {
            if (S.charAt(curIdx) == '0' && i > curIdx) {
                break;
            }
            long num = Long.valueOf(S.substring(curIdx, i + 1));
            if (num > Integer.MAX_VALUE) {
                break;
            }
            if (result.size() <= 1 || num == (long) result.get(result.size() - 1) + (long) result.get(result.size() - 2)) {
                result.add((int) num);
                if (splitIntoFibonacciFrom(i + 1, result, S)) {
                    return true;
                }
                result.remove(result.size() - 1);
            }
        }
        return false;
    }
