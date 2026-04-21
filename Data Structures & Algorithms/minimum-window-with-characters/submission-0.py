class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def getdict(t):
            T = defaultdict(int)

            for char in t:
                T[char] += 1
            
            return T

        def condition(T,D):
            for key, value in T.items():
                if D.get(key,0) < value:
                    return False
            return True

        

        left = 0
        result = None
        minlen = float('inf')
        T = getdict(t)

        D = defaultdict(int)

        for right in range(len(s)):
            D[s[right]] += 1

            while condition(T, D):  
                if minlen > right - left + 1:
                    minlen = right - left + 1
                    result = s[left:right+1]
                D[s[left]] -= 1
                left += 1

        return result if result is not None else ""

        