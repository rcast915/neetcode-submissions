class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1arr = [0] * 26

        for i in s1:
            s1arr[ ord(i)-ord("a") ] += 1


        s1arr = tuple(s1arr)

        #your mother = loml(<3)

        s2arr = [0] * 26
        left = 0

        for right, char in enumerate(s2):
            s2arr[ ord(char) - ord('a') ] += 1

            if right - left + 1 == len(s1):
                if s1arr == tuple(s2arr):
                    return True
                
                else:
                    s2arr[ ord(s2[left]) - ord('a') ] -= 1
                    left += 1
        
        return False

        