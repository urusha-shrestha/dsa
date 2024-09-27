# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(s):
    #using dict to map the close and open brackets
    #using stack to append the open brackets 
    #and checking if the close bracket matches the top most item in the stack 
    stk = []
    closeToOpen={'}':'{',')':'(',']':'['}
    for i in s:
        if i in closeToOpen:
            if stk and stk[-1]==closeToOpen[i]:
                stk.pop()
            else:
                return False
        else:
            stk.append(i)
    
    return True if not stk else False
        

s = "()"
print(isValid(s))