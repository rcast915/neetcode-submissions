from collections import defaultdict, deque
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0

        count = 0
        visited = set()
        graph = defaultdict(list)

        # FIX 1: Add edges in BOTH directions (undirected graph)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)


        # for each node 
        for i in range(n):
            # check if node has been seen
            if i in visited:
                continue
            
            # BFS
            # FIX 2: Pass the integer as a list so it's iterable
            q = deque([i])
            visited.add(i)

            # FIX 3: Use colon and indentation instead of {
            while len(q) != 0:
                # FIX 4a: Use popleft() for BFS
                node = q.popleft()

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        # FIX 5: Mark visited as soon as it goes in the queue
                        visited.add(neighbor)
                        # FIX 4b: Use append() instead of add()
                        q.append(neighbor)
            # } <- Removed curly brace

            # Add component
            count += 1
        
        return count

        