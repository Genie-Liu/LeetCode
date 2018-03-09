class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = int((low + high) / 2)
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        rot = high
        r1 = self._search(nums, 0, rot - 1, target)
        if r1 != -1:
            return r1
        r2 = self._search(nums, rot, len(nums) - 1, target)
        if r2 != -1:
            return r2
        return -1

    def _search(self, nums, low, high, target):
        while low < high:
            mid = int((low + high) / 2)
            if nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        if nums[high] == target:
            return high
        else:
            return -1
