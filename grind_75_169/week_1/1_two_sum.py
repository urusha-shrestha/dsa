# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def two_sum(nums, target):
    #using two pointer method to point one to the current index of the iteration
    #and the second to the last index of he list and decreasing it till it matches the current index of iteration
    for i in range(len(nums)):
        last= len(nums)-1
        while last>i:
            if nums[i]+nums[last] == target:
                return([i,last])
            else:
                last -= 1
    return []


nums = [2,7,11,15]
target = 9

print(two_sum(nums,target))