# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

def longestSubstring(s):
    start = 0
    end = 0
    longestSubstring = 0
    subStringMap = {}

    for end in range (len(s)):
        char = s[end]
        if (char not in subStringMap) or (subStringMap[char]==False):
            subStringMap[char] = True
            longestSubstring = max(longestSubstring, (end - start + 1))
        else:
            while subStringMap[char] == True:
                subStringMap[s[start]] = False
                start += 1
            subStringMap[char] = True
    
    return longestSubstring

s = "tmmzuxt"
print(longestSubstring(s))