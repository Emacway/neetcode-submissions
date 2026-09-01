class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        if strs == []:
            return result
        for string in strs:
            count = len(string)
            result += str(count)
            result += '#'
            result += string
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        i = 0
        result = []
        while (i < len(s)):
            digits = s[i]
            while (s[i + 1] != '#'):
                digits += s[i + 1]
                i += 1
                
            length = int(digits)
            string = s[(i + 2) : (i + 2 + length)]
            result.append(string)
            i += length + 2
        return result



