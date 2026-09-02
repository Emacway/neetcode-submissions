class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                if i == len(s) - 1: #can't end on an open parentheses
                    return False
            elif s[i] == '{':
                stack.append(s[i])
                if i == len(s) - 1: #can't end on an open parentheses
                    return False
            elif s[i] == '[':
                stack.append(s[i])
                if i == len(s) - 1: #can't end on an open parentheses
                    return False
            elif s[i] == ')':
                if stack != []:
                    popped = stack.pop()
                    if popped != '(':
                        return False
                else: #if stack is empty, we can't start on a closed parentheses
                    return False
            elif s[i] == '}':
                if stack != []:
                    popped = stack.pop()
                    if popped != '{':
                        return False
                else: #if stack is empty, we can't start on a closed parentheses
                    return False
            elif s[i] == ']':
                if stack != []:
                    popped = stack.pop()
                    if popped != '[':
                        return False
                else: #if stack is empty, we can't start on a closed parentheses
                    return False
        if stack == []:
            return True #we found all matches
        else:
            return False