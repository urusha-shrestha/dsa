# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

#Two pointer solution
def strStr(haystack: str, needle: str) -> int:
    p1 = 0
    p2 = 0
    trueCount = 0
    while p1 < len(haystack):
        if (haystack[p1] == needle[p2]):
            trueCount += 1
            if trueCount == len(needle):
                return (p1-len(needle) +1)
            p1 += 1
            p2 += 1
        else:
            if p2 == 0:
                p1 += 1
            else:
                p1 = p1 - trueCount +1
                p2 = 0
            
            trueCount = 0
            
    return -1



# Second solution

def str2(haystack, needle):
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            if haystack[i:i+len(needle)] == needle:
                return i
    return -1 


haystack = "mississippi"
needle = "issip"

print(strStr(haystack,needle))
print(str2(haystack, needle))