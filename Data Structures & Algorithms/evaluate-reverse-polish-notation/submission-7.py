class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # recursive solution
        def evalRec():
            res = tokens.pop()

            if res not in "+-*/":
                return int(res)

            right = evalRec()
            left = evalRec()

            if res == "+":
                return left + right

            elif res == "-":
                return left - right

            elif res == "*":
                return left * right

            elif res == "/":
                return int(left / right)

        return evalRec()