# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

nums1 = [1,3]
nums2 = [2]

def findMedian(nums1, nums2):
    arrIndex1 = 0
    arrIndex2 = 0
    merged = []
    while arrIndex1<len(nums1) and arrIndex2<len(nums2):
        if nums1[arrIndex1] < nums2[arrIndex2]:
            merged.append(nums1[arrIndex1])
            arrIndex1 += 1
        else:
            merged.append(nums2[arrIndex2])
            arrIndex2 += 2

    return merged

print(findMedian(nums1,nums2))