
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         answer = defaultdict(int)
#         length = len(temperatures)
#         check = [False]*length
        
#         for i in range(1,length):
#             for j in temperatures[i:]:
#                 if j > temperatures[i-1]:
#                     answer[i-1] +=1
#                     check[i-1] = True
#                     break
#                 answer[i-1] +=1 
        
#         for i in [_ for _, x in enumerate(check) if not x]:
#             answer[i] = 0   
    
#         return answer.values()


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        
        for i,x in enumerate(temperatures):
            while stack and x > temperatures[stack[-1]]:
                curr = stack.pop()
                answer[curr] = i - curr
            stack.append(i)
        return answer

        #faster version (monotonic stack)