
import heapq
import math
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        output = []

        for cord in points:
            distance = math.sqrt((cord[0] - 0) ** 2 + (cord[1] - 0) ** 2)
            distance_tuple = (-distance, cord)

            if len(heap) == k:
                heapq.heappushpop(heap, distance_tuple)
            else:
                heapq.heappush(heap, distance_tuple)

        for item in heap:
            output.append(item[1])

        return output

# Example usage:
points = [[3, 3], [5, -1], [-2, 4]]
k = 2
solution = Solution()
result = solution.kClosest(points, k)
print(result)  # Output: [[3, 3], [-2, 4]]

points = [[1, 3], [-2, 2]]
k = 1
solution = Solution()
result = solution.kClosest(points, k)
print(result)  # Output: [[-2, 2]]

points = [[1, 1], [1, 1], [1, 1], [0, 0]]
k = 2
solution = Solution()
result = solution.kClosest(points, k)
print(result)  # Output: [[0, 0], [1, 1]]