# class Solution:
#     def decodeString(self, s: str) -> str:
#         start, end = 0,0
#         while '[' in s:
#             for i in range(len(s)):
#                 if s[i].isdigit():
#                     multiple = s[i]
#                 if s[i] == '[':
#                     start = i
#                 if s[i] == ']':
#                     end = i
#                 if start !=0 and end != 0:
#                     s.replace(s[start:end+1],int(multiple)*s[start+1:end])
#             return self.decodeString(s)
#         return s

#Referenced from leetcode
class Solution:
    def decodeString(self, s: str) -> str:
        words, num, chunk = [], 0 ,''
        for i in s:
            if i == '[':
                words.append(chunk)
                words.append(num)
                chunk = ''
                num = 0
            elif i == ']':
                nums = words.pop()
                prev = words.pop()
                chunk = prev + nums*chunk
            elif i.isdigit():
                num = num*10 + int(i)
            else:
                chunk += i
        return chunk

# class Solution:
#     def decodeString(self, s: str) -> str:
#         words, num = [],[]
#         chunk = ''
#         for i in range(len(s)):
#                 if s[i].isdigit():
#                     multiple.append(int(s[i]))
#                 elif s[i] == '[':
#                     words.append(s[i])
#                 elif s[i] == ']':
#                     words.append(chunk*multiple.pop())
#                     chunk = ''
#                 else:
#                     chunk += s[i]
#         return words+chunk