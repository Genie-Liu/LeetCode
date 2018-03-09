class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # j = len(nums)-1
        j = len(nums)-2
        i = j + 1

        while j >= 0:
            if nums[j] < nums[j+1]:
                break
            j -= 1
        if j < 0:
            nums.sort()
        else:
            for i in range(len(nums)-1, j, -1):
                if nums[i] > nums[j]:
                    break
            tmp = nums[j]
            nums[j] = nums[i]
            nums[i] = tmp
            nums[j+1:] = sorted(nums[j+1:])