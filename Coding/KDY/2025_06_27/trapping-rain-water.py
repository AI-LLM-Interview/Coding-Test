class Solution(object):
    def trap(self, height):
        result = 0
        idx_l = 0
        idx_r = len(height) - 1
        max_l = 0               
        max_r = 0

        while idx_l < idx_r:
            if height[idx_l] < height[idx_r]:
                if height[idx_l] >= max_l:
                    max_l = height[idx_l]
                else:
                    result += max_l - height[idx_l]
                idx_l +=1
            
            else:        
                if height[idx_r] >= max_r:
                    max_r = height[idx_r]
                else:
                    result += max_r -height[idx_r]
                idx_r -= 1
        return result