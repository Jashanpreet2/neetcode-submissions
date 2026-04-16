class Solution:
    def trap(self, height: List[int]) -> int:
        # first = 0
        # total_water = 0

        # while first < len(height) and height[first] == 0:
        #     first += 1
        
        # while first < len(height) - 1:
        #     so_far = 0
        #     second = first
        #     biggest_index = first + 1
        #     while second < len(height) - 1 and (height[second] < height[first] or biggest_index is None):
        #         second += 1
        #         so_far += height[second]
        #         if height[second] > height[biggest_index]:
        #             biggest_index = second
        #     add = min(height[first], height[biggest_index]) * (biggest_index - first - 1)
        #     total_water += add
        #     total_water -= (so_far - height[biggest_index]) if (so_far - height[biggest_index]) <= add else add
        #     first = biggest_index
        # return total_water
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        res = 0

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                res += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]
        
        return res

        