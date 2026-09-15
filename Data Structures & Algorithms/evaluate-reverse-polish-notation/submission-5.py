class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            res = int(tokens.pop())
        stack = []
        
        for token in tokens:
            if token == "+":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                res = num1 + num2
                stack.append(str(res))
                
            elif token == "-":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                res = num1 - num2
                stack.append(str(res))
                
            elif token == "*":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                res = num1 * num2
                stack.append(str(res))
                
            elif token == "/":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0):
                    res = num1 // num2
                else:
                    res = -((-num1) // num2) #always truncate toward 0
                stack.append(str(res))
                
            else: #numeric tokens
                stack.append(token)
                
        
        return res
