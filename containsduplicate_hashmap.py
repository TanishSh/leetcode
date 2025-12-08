# Initialize an empty hash set to store seen values.
# Iterate through each number in the array.
# For each number:
# If it is already in the set, return True because a duplicate has been found.
# Otherwise, add it to the set.
# If the loop finishes without finding any duplicates, return False.

# Time complexity: O(n) as just loop through the list
# set don't contain duplicate values, if add duplicates then python just ignores it

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num) # .add() instead of .apppend() like in list

        return False