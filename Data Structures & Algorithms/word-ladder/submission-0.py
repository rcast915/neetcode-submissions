class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def constructdict(wordList):
            D = defaultdict(list)
            
            for word in wordList:
                for index in range(len(word)):
                    pattern = word[:index] + "*" + word[index+1:]
                    D[pattern].append(word)
            
            return D
            
           
        wordList.append(beginWord)
        D = constructdict(wordList)
    
        
        visited = set()
        q = deque()
        q.append((beginWord,1))
        visited.add(beginWord)
        
        while q:
            word, distance = q.popleft()
            
            if word == endWord:
                return distance
            
            for index in range(len(word)):
                pattern = word[:index] + "*" + word[index+1:]
                for w in D[pattern]:
                    if w not in visited:
                        q.append((w,distance+1))
                        visited.add(w)
            
                
                    
        return 0
            
        
        