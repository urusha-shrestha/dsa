# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(s):
    stk = []
    closeToOpen= {'}':'{',
                  ')':'(',
                  ']':'['}
    
    for i in s:   #iterate through the string
        if i in closeToOpen:  #if i is a closing bracket
            if stk and stk[-1]==closeToOpen[i]:
                #if the stack is not empty and 
                #the last element in the stack is the opening bracket for the current closing bracket
                stk.pop()
            else:
                return False
        else:   #if i is an opening bracket, add to the stack
            stk.append(i)

    return True if not stk else False 
    #return True if stk is empty

s="{([])}"
print(isValid(s))
    
