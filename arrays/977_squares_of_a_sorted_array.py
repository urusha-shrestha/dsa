# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

#Iterating method
def sortedSquaresIter(nums):
    arr=[]
    for i in nums:
        arr.append(i**2)
    arr.sort()
    return arr

#Two pointer method
def sortedSquaresTwoPtr(nums):
    N=len(nums)
    arr=[0]*N
    left, right=0, N-1
    ptr=N-1

    while left <= right:
        l2 = nums[left] **2
        r2 = nums[right]**2
        if l2<r2:
            arr[ptr]=r2
            right -= 1
        else:
            arr[ptr]=l2
            left += 1
        ptr -= 1
    return arr
    


nums=[-4,-1,0,3,10]

print(sortedSquaresTwoPtr(nums))