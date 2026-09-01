class Solution:

    def encode(self, strs: List[str]) -> str:
        #if list is empty, return empty string
        if not strs: 
            return ""

        #initialize
        sizes, res = [], []

        #iterate through list of strings, get list of sizes
        for s in strs:
            sizes.append(len(s))
        
        #iterate through list of sizes, append to result string
        for sz in sizes:
            res.append(str(sz))
            res.append(',') #delimiter
        res.append('#') #delimiter for end of sizes
        res.extend(strs) # add all strings to res
        return ''.join(res) #makes one string of strings without delimiter

    def decode(self, s: str) -> List[str]:
        # if string is empty, return empty list
        if not s:
            return []
        
        #initializing
        sizes, res, i = [], [], 0

        #iterate through the sizes
        while s[i] != '#':
            j = i
            while s[j] != ',': #get all digits of number
                j += 1
            sizes.append(int(s[i:j])) #build sizes array
            i = j + 1 #go to next size
        
        # we got to the '#', now look at next character
        i += 1

        # iterate through the sizes in the sizes array
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz #jump to next string
        return res

