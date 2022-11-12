visited = {}  # Initialize a dictionary to act a Python "hash map"
​
for i, value in enumerate(nums):  # For loop alternative, gives index (i) and value (nums[i])
​
toFind = target - value  # Calculates amount needed still
​
visited[value] = i  # Add the current value to the 'hash map'