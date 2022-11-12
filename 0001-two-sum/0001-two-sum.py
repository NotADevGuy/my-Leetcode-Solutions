class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = {}
        
        for i, value in enumerate(nums):
            toFind = target - value
            
            if toFind in visited:
                return [i, visited[toFind]]
            else:
                visited[value] = i