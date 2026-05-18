class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return -1

        m = len(nums)//2

        val = nums[m]

        if val == target:
            return m
        elif val != target and len(nums)==1:
            return -1

        if val < target: # go right
            result = self.search(nums[m+1::], target)
            if result == -1:
                return -1
            else: 
                return m + result + 1
        elif val > target: # go left
            return self.search(nums[:m:], target)

        return -1
        