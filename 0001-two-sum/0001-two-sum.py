class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = {}  # Initialize a dictionary to act as a python hash map
        
        for i, value in enumerate(nums):  # Enumerate goes through list index and values respectively
            toFind = target - value  # This does the math to figure out what number needs to be found still
            
            if toFind in visited:  # If the value from above is found as a key in the 'hash map', then...
                return [i, visited[toFind]]  # Return the index of current value and the index of the found value
            else:  # Otherwise, ...
                visited[value] = i  # Add the current value to the 'hash map'