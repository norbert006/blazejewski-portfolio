def isValid(s):
    stack = []
    closeToOpen = { ")": "(", "}": "{", "]": "["}

    for bracket in s:
        if bracket in closeToOpen:
            if stack and stack[-1] == closeToOpen[bracket]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)
    
    if not stack:
        return True
    else:
        return False

print(isValid("([)]"))

'''
Line 5: For every character (bracket) in the String.
Line 6: Check if the character is a closing bracket (this is why every Key in the map is a closing bracket).
Line 7: If it is a closing bracket, make sure that the stack is not empty and check that the value at the top
        of the stack is the matching bracket. Stack[-1] is the most recent value that has been added to the stack.
Line 15: Only return True if the stack is empty. Otherwise, if any bracket remains in the stack, it means that a
        closing bracket was missing.

'''