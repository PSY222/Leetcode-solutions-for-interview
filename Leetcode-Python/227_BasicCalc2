class Solution:
    def calculate(self, s: str) -> int:
        sign = "+"
        curr = 0
        stack = []

        for i,ss in enumerate(s):
            if ss.isdigit():
                curr = 10*curr + int(ss)
            if ss in "+-*/" or i == len(s)-1:
                if sign =="+":
                    stack.append(curr)
                elif sign =="-":
                    stack.append(-curr)
                elif sign =="*":
                    stack.append(stack.pop()*curr)
                elif sign == "/":
                    stack.append(int(stack.pop()/curr))
                sign, curr = ss, 0
        return sum(stack)