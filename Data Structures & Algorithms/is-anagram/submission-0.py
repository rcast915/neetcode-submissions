class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        d = defaultdict(int)

        for char_s in s:
            d[char_s] += 1
        
        for char_t in t:
            d[char_t] -= 1
        

        for values in d.values():
            if values != 0:
                return False
        return True


        