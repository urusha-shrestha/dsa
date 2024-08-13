# You are given a 0-indexed integer array nums and an integer k. 
# Your task is to perform the following operation exactly k times in order to maximize your score:

# 1. Select an element m from nums.
# 2. Remove the selected element m from the array.
# 3. Add a new element with a value of m + 1 to the array.
# 4. Increase your score by m.
# Return the maximum score you can achieve after performing the operation exactly k times.

def maximizeSum(nums,k):
    m=0
    a=nums[0]
    d=1
    for i in range(len(nums)):
        if nums[i]>a:
            a=nums[i]
    m=k*(2*a + ((k-1)*d))/2
    return (int(m))


nums=[1,2,3,4,5]
k=3

print(maximizeSum(nums,k))