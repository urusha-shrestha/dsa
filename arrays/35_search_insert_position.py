
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

def searchInsert(nums, target):
    l=0
    r= len(nums)-1
    
    while l<=r:
        mid = (l+r)//2
        if (target==nums[mid]):
            return mid
        elif (nums[mid]<target):
            l = mid+1
        else:
            r = mid-1
    return l 
nums = [1,3,5,6]
target = 7

print(searchInsert(nums,target))