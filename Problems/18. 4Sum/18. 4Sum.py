class Solution:
    # find N Sum version
    def findSum(self, nums, target, N, result, results):
        if N < 2 or len(nums) < N or nums[0]*N > target or nums[-1]*N < target:
            return None
        if N == 2:
            l, r = 0, len(nums)-1
            while l < r:
                if l > 0 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while r > l and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s > target:
                    r -= 1
                else:
                    l += 1
        else:
            for i in range(len(nums)-N+1):
                if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                    self.findSum(nums[i+1:], target-nums[i], N-1, result + [nums[i]], results)
        return results

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rlt = []
        self.findSum(sorted(nums), target, 4, [], rlt)

        return rlt




