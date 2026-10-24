# Kth Largest Element in a Stream

# Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

# Implement the following methods:

# constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
# int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.

import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k

        # make a heap fromm the initial numbers
        self.heap = nums[:]
        heapq.heapify(self.heap)

        # keep only the k largest values
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.heap)


        return self.heap[0]
        
