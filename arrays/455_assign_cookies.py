# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a 
# size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. 
# Your goal is to maximize the number of your content children and output the maximum number.


g = [3,2,1]
s = [1,1]

def contentChildren(g,s):
    cookiesLength = len(s)
    if cookiesLength == 0:
        return 0
    
    g.sort()
    s.sort()

    gIndex = len(g) - 1
    sIndex = cookiesLength - 1
    maxNum = 0

    while gIndex>=0 and sIndex>=0:
        if (s[sIndex]>=g[gIndex]):
            maxNum += 1
            sIndex -= 1
        gIndex -= 1
    
    return maxNum

print(contentChildren(g,s))