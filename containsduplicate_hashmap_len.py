# Convert the array into a hash set, which removes duplicates.
# Compare the size of the set with the size of the original array.
# If the set is smaller, return True because duplicates must have been removed.
# Otherwise, return False.

# Time complexity: O(n) as just loop through the list

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = len(set(nums)) < len(nums)
        return result