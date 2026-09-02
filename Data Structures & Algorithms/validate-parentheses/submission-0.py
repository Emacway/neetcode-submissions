class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        else:
            if "{}" in s:
                newS = s.replace("{}", "")
                return self.isValid(newS)
            elif "[]" in s:
                newS = s.replace("[]", "")
                return self.isValid(newS)
            elif "()" in s:
                newS = s.replace("()", "")
                return self.isValid(newS)
            else:
                return False
            