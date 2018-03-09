class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = j = 0
        n = len(nums)
        while j < n:
            while j > 0 and j < n and nums[j] == nums[j-1]:
                j += 1
            if j < n:
                nums[i] = nums[j]
                i += 1
                j += 1

        return i
