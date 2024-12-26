# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

def isHappy(n):
    lst = []
    lst.append(n)
    while (len(str(n))) != 0:
        if (n == 1):
            return True
        num = 0
        for i in (str(n)):
            num += int(i)**2 
        print(num)
        n =  num
        if (num in lst):
            return False
        lst.append(num)
    return True

n = 1
print(isHappy(n)) 