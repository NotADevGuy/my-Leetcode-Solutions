class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for x in range(len(nums)):
                if nums[i] + nums[x] == target and i != x:
                    return [i, x]