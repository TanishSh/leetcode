import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Max-heap via negation
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)  # largest
            x = -heapq.heappop(heap)  # second largest
            if x != y:
                heapq.heappush(heap, -(y - x))

        if len(heap) == 0:
            return 0
        return -heap[0]