class Solution:
    def trap(self, height: List[int]) -> int:
        # l, r pointers
        lp, rp = 0, 0
        sum = 0

        while lp < len(height) and rp < len(height):
            while rp+1 < len(height) and height[rp+1] < height[lp]:
                rp += 1 

            if rp >= len(height) - 1:
                lp += 1
                rp = lp
                continue

            # sum pointer
            sp = lp+1 
            while sp <= rp:
                sum += (height[lp] - height[sp])
                sp += 1

            lp = rp + 1
            rp = lp
        
        return sum

