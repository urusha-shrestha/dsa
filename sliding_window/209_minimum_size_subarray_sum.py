# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

def minSubArraySum(target, nums):
    start = 0
    end = 0
    minLength = 0
    subSum = 0

    for end in range (len(nums)):
        subSum += nums[end]

        while subSum>=target:
            if minLength == 0:
                minLength = end-start+1
            minLength = min(minLength, (end-start+1))
            subSum -= nums[start]
            start += 1
    return minLength

target = 7
nums = [2,3,1,2,4,3]
print(minSubArraySum(target, nums))