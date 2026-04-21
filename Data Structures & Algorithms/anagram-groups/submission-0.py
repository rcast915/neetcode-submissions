from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            key = [0] * 26

            for char in word:
                indx = ord(char) - ord("a")
                key[indx] += 1
                
            d[tuple(key)].append(word)

        l = []
        for keys, lists in d.items():
            l.append(lists)

        return l        
        
        
            



        