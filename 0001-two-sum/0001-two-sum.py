class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = range(len(nums))
        for i in length:
            for x in length:
                if nums[i] + nums[x] == target and i != x:
                    return [i, x]
#                 hello