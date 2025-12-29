# ------------------------------------ my solution which is non-hash map 
# (also similar to hash map, two pass official solution)----------------------------------
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li = [] #malloc
        for i, num in enumerate(nums): # index, value
            diff = target - num
            i_2 = nums.index(diff)
            if (diff in nums) and (i_2 != i):
                li.append(i)
                li.append(i_2)

                return li
            
# sorting: 2 pointer solution
# Create a copy of the array and sort it in ascending order.
# Initialize two pointers, one at the beginning and one at the end of the array.
# Iterate through the array with the two pointers and check if the sum of the two numbers is equal to the target.
# If the sum is equal to the target, return the indices of the two numbers.
# If the sum is less than the target, move the left pointer to the right, which will increase the sum.
# If the sum is greater than the target, move the right pointer to the left, which will decrease the sum.
# There is guaranteed to be exactly one solution, so we will never return an empty array.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()

        # 2 pointers
        i, j = 0, len(nums) - 1

        while i < j:
            a1 = A[i][0] 
            a2 = A[j][0]
            curr = A[i][0] + A[j][0]
            if curr == target:
                return (min(a1, a2), max(a1, a2))
            
            # update the 2 pointers
            elif curr < target:
                i += 1 # curr < target, so move left pointer to inc. currer
            else:
                j+= 1 # curr < target, so move right  pointer to inc. curr

        return []
    
# hash map, two pass
# -------------- hash map, two pass algorithm ------------
# Create a hash map to store the value and index of each element in the array.
# Iterate through the array and compute the complement of the current element, which is target - nums[i].
# Check if the complement exists in the hash map.
# If it does, return the indices of the current element and its complement.
# If no such pair is found, return an empty array.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} #{ num: index}

        for i, n in enumerate(nums): # enumerate: index, value
            indices[n] = i 

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [indices[diff], i]
            
        return []



        