class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]
        lower = 0
        upper = len(nums) - 1

        while lower < upper:
            mid = int((lower + upper) / 2)
            if nums[mid] > target:
                upper = mid
            elif nums[mid] < target:
                lower = mid + 1
            else:
                lower = upper = mid
        if nums[lower] != target:
            return [-1, -1]

        while lower > 0 and nums[lower] == target:
            lower -= 1
        if nums[lower] != target:
            lower += 1

        while upper < len(nums) - 1 and nums[upper] == target:
            upper += 1
        if nums[upper] != target:
            upper -= 1

        return [lower, upper]
