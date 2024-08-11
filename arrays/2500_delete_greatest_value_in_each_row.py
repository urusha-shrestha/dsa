# You are given an m x n matrix grid consisting of positive integers.

# Perform the following operation until grid becomes empty:

# Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
# Add the maximum of deleted elements to the answer.
# Note that the number of columns decreases by one after each operation.

# Return the answer after performing the operations described above.

def deleteGreatestValue(grid):
    counter=0
    while (len(grid[0]) != 0):
        greater = []
        for i in range(len(grid)):
            largest = grid[i][0]
            grid[i].sort()
            largest = grid[i][-1]
            greater.append(largest)
            del (grid[i][-1])
        greater.sort()
        counter = counter + greater[-1]
    
    print(counter)
        


grid = [[1,2,4],[3,3,1]]

deleteGreatestValue(grid)
