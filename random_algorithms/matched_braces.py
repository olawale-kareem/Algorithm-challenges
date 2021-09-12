# matched braces
def validBraces(string):
    stack = []
    for bracket in string:
        # always push in open parenthesis
        if bracket == "(" or bracket == "{" or bracket == "[":
            stack.append(bracket)
        else:
            # the first line takes care of a scenerio when a closing parenthesis starts the arrangement
            # just exit with a false else continue
            if len(stack) == 0:
                return False 
            if bracket == ")":
                if stack[len(stack) - 1] == "(":
                    stack.pop()
            elif bracket == "}":
                if stack[len(stack) - 1] == "{":
                    stack.pop()
            else:
                if stack[len(stack) - 1] == "[":
                    stack.pop()   
    # the initial return false from the for loop will overide the return satement in this block
    if len(stack) > 0:
        return False
    else:
        return True

# test cases
print(validBraces("[({})](]" ))
print(validBraces("([{}])" ))
print(validBraces("(){}[]"))
print(validBraces( "(}"))
print(validBraces( "[(])" ))
print(validBraces( "])[(" ))