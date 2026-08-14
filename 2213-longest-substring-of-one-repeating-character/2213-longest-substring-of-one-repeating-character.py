from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        
        # tree[i] = [size, pref_char, pref_len, suff_char, suff_len, max_len]
        # Using a flat list for nodes to heavily optimize Python overhead
        tree = [[0, '', 0, '', 0, 0] for _ in range(4 * n)]
        
        def merge(node: int, left: int, right: int) -> None:
            L = tree[left]
            R = tree[right]
            
            size = L[0] + R[0]
            
            # Calculate Prefix
            pref_char = L[1]
            pref_len = L[2]
            if L[2] == L[0] and L[1] == R[1]:
                pref_len += R[2]
                
            # Calculate Suffix
            suff_char = R[3]
            suff_len = R[4]
            if R[4] == R[0] and R[3] == L[3]:
                suff_len += L[4]
                
            # Calculate Max Length (either fully in left, fully in right, or crossing the boundary)
            max_len = max(L[5], R[5])
            if L[3] == R[1]:
                max_len = max(max_len, L[4] + R[2])
                
            tree[node] = [size, pref_char, pref_len, suff_char, suff_len, max_len]
            
        def build(node: int, l: int, r: int) -> None:
            if l == r:
                # Leaf node representing a single character
                tree[node] = [1, s[l], 1, s[l], 1, 1]
                return
            mid = (l + r) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            build(left_child, l, mid)
            build(right_child, mid + 1, r)
            merge(node, left_child, right_child)
            
        def update(node: int, l: int, r: int, idx: int, char: str) -> None:
            if l == r:
                # Update the character at the leaf node
                tree[node][1] = char
                tree[node][3] = char
                return
            mid = (l + r) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            if idx <= mid:
                update(left_child, l, mid, idx, char)
            else:
                update(right_child, mid + 1, r, idx, char)
                
            merge(node, left_child, right_child)
            
        # Build the initial segment tree
        build(0, 0, n - 1)
        
        ans = []
        for char, idx in zip(queryCharacters, queryIndices):
            # Process each query
            update(0, 0, n - 1, idx, char)
            # The root node (0) will always hold the max_len for the entire string
            ans.append(tree[0][5])
            
        return ans