class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return 0
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = int((low + high) / 2)
            if nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        if nums[low] < target:
            return low + 1
        else:
            return low
