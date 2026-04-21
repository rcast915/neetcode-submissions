class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ""
        string = str(len(strs[0])) + ":" + strs[0]

        for i in strs[1:]:
            string = string + str(len(i)) + ":" + i
        
        return string

    def decode(self, s: str) -> List[str]:
        l = []

        i = 0
        while i < len(s):
            j = i

            while s[j] != ":":
                j += 1
            
            length = int(s[i:j])

            l.append(s[j+1:j+length + 1])
            i = j+length +1 
        
        return l