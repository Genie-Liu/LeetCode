class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums: return 0
        i = j = len(nums)-1
        for i in range(j, -1, -1):
            if nums[i] == val:
                self.exchange(nums, i, j)
                j -= 1
        return j+1

    def exchange(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = nums[i]

