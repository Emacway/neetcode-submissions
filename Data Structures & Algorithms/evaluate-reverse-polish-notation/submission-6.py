class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #maintain a stack of integers instead of strings
        if len(tokens) == 1:
            res = int(tokens.pop())
        stack = []
        
        for token in tokens:
            if token == "+":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                res = num1 + num2
                stack.append(res)
                
            elif token == "-":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                res = num1 - num2
                stack.append(res)
                
            elif token == "*":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                res = num1 * num2
                stack.append(res)
                
            elif token == "/":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0):
                    res = num1 // num2
                else:
                    res = -((-num1) // num2) #always truncate toward 0
                stack.append(res)
                
            else: #numeric tokens
                stack.append(int(token))
                
        
        return res