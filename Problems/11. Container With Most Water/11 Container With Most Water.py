class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0

        # set i and j to the end of list
        i = 0
        j = len(height) - 1
        while i < j:
            max_area = max(max_area, min(height[i], height[j])*(j-i))

            # move the lower side to innen list
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area
