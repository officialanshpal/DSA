import collections
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build the adjacency list for the directed graph
        adj = collections.defaultdict(list)
        for u, v in invocations:
            adj[u].append(v)
            
        # Step 2: Use BFS to find all suspicious methods starting from k
        suspicious = set()
        queue = collections.deque([k])
        suspicious.add(k)
        
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        # Step 3: Check if any non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                # Removal is not possible, return all methods
                return list(range(n))
                
        # Step 4: Return all methods that are not suspicious
        return [i for i in range(n) if i not in suspicious]