# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s):
    i = 0
    j = len(s)-1
    while i<j:
        if s[i].lower() == s[j].lower():
            i += 1
            j -= 1
        elif s[i].isalnum() == False:
            i += 1
        elif s[j].isalnum() == False:
            j -= 1
        else:
            return("False")
    return("True")

s="A man, a plan, a canal: Panama"

print(isPalindrome(s))
        