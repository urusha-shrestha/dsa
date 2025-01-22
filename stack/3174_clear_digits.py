# You are given a string s.

# Your task is to remove all digits by doing this operation repeatedly:

# Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.

def clearDigits(s):
    stk=[]
    for i in s:
        if i.isdigit():
            stk.pop()
        else:
            stk.append(i)
    return "".join(stk)

s="abc"
print(clearDigits(s))