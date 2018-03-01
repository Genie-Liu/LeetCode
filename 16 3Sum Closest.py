class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        rlt = sum(nums[0:3])
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(rlt - target):
                    rlt = s
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    return target
        return rlt
