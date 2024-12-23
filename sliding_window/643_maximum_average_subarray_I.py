# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
import math 

def maxSubArray(k, nums):
    start = 0
    end = 0
    windowSum = 0
    sumMax = -math.inf

    for end in range(len(nums)):
        windowSum += nums[end]

        if ((end-start+1)==k):
            sumMax = max(sumMax, windowSum/k)
            windowSum -= nums[start]
            start += 1
    
    return sumMax 

k = 4
nums = [1,12,-5,-6,50,3]

print(maxSubArray(k,nums))