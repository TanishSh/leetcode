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