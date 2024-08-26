# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

def shuffleArr(nums, n):
    x=0
    y=n
    arr=[]
    while x<3:
        arr.append(nums[x])
        arr.append(nums[y])
        x +=1
        y +=1
    return arr

nums=[2,5,1,3,4,7]
n=3

print(shuffleArr(nums,n))