# ------------------------------------ my solution ----------------------------------
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