from collections import defaultdict
from typing import List

class Solution:
    def maxXorInNonOverlappingSubtrees(self, n: int, edges: List[List[int]], values: List[int]) -> int:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # Compute the subtree sums using DFS
        subtree_sum = [0] * n
        def dfs(node, parent):
            subtree_sum[node] = values[node]
            for neighbor in tree[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    subtree_sum[node] += subtree_sum[neighbor]

        dfs(0, -1)  # Start DFS from the root (node 0)

        # Compute the maximum XOR of non-overlapping subtrees
        max_xor = 0
        seen_sums = set()

        def dp(node, parent):
            nonlocal max_xor, seen_sums
            current_sum = subtree_sum[node]

            # Clear the seen_sums set before processing each child of the root
            if parent == 0:
                seen_sums.clear()

            # Check all previously seen subtree sums for maximum XOR
            for s in seen_sums:
                max_xor = max(max_xor, current_sum ^ s)

            # Add current subtree sum to the seen set
            seen_sums.add(current_sum)

            for neighbor in tree[node]:
                if neighbor != parent:
                    dp(neighbor, node)

            # Remove current subtree sum after processing to backtrack
            seen_sums.remove(current_sum)

        # Start dynamic programming from each child of the root separately to ensure non-overlapping
        for child in tree[0]:
            dp(child, 0)

        return max_xor

# Example usage
solution = Solution()
n = 3
edges = [[0,1],[1,2]]
values = [4,6,1]
print(solution.maxXorInNonOverlappingSubtrees(n, edges, values))  # Expected Output: 24