def goodPairs(nums):
    l=0
    r=len(nums)-1
    counter=0
    while l<len(nums)-1:
        r=len(nums)-1
        while l<r:
            if nums[l]==nums[r]:
                counter += 1
            r -= 1
        l += 1
    return counter
    
        

nums = [1,1,1,1]
print(goodPairs(nums))