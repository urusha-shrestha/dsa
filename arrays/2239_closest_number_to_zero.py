# Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
# If there are multiple answers, return the number with the largest value.


def closest_to_zero(nums):
    closest = nums[0]

    for i in nums:
        if abs(i) < abs(closest):
            closest = i
        elif abs(i) == abs(closest):
            if i>closest:
                closest = i
    return closest



nums = [-4,-2,2,4,8]
n = closest_to_zero(nums)

print(n)
