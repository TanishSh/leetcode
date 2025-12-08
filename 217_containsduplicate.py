# Sort the array in non-decreasing order.
# Iterate through the array starting from index 1.
# Compare the current element with the previous element.
# If both elements are equal, we have found a duplicate — return True.
# If the loop finishes without detecting equal neighbors, return False.

#Time complexity: O(nlogn) -> as sort takes O(nlogn) in general/worst case
# loop later only O(n) which is < O(nlogn) -> so O(nlogn) dominates
# O(nlogn + n) = O(nlogn)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True

        return False
        
# brute force -> check all pairs, each item starting at index 0... n-1 to all others items -> 0(n^2)

