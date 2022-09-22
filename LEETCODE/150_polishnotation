class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        f = []
        
        while tokens:
            for i in tokens:
                if i == "+":
                        n = f.pop()
                        m = f.pop()
                        f.append(int(n)+int(m))
                elif i == "-":
                        n = f.pop()
                        m= f.pop()
                        f.append(int(m)-int(n))
                elif i == "*":
                        n = f.pop()
                        m= f.pop()
                        f.append(int(n)*int(m))
                elif i == "/":
                        n = f.pop()
                        m = f.pop()
                        f.append(int(m)/int(n))
                else:
                        f.append(i)
                
            return int(f[0])