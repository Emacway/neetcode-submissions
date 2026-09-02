class Solution:
    def isValid(self, s: str) -> bool:
        #neater code using the stack method
        stack = []
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in closeToOpen: #a close parentheses
                if stack and stack[-1] == closeToOpen[c]: #nonempty stack and peek at corresponding open parentheses
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack #if stack is empty we matched all parentheses!