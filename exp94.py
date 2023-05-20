def checksvalid(str1):
    count = 0
    ans = False
    for i in str1:
        if i == "(" or i == "{" or i == "[":
            count += 1
        elif i == ")" or i == "}" or i == "]":
            count -= 1
        if count < 0:
            return ans
    if count==0:
        return not ans
    return ans
str1 = input("Enter the input string: ")
print("Checks the input string valid or Not? :",checksvalid(str1)) 


def checkBalance(expr):
    stack = []
    for char in expr:
        if chafr in ["(", "{", "["]:
            stack.append(char)
        else:
            #here we check if the current character is
            #bracket, then it must be closing'
            #so stack cannot be empty at his point.
            print(not stack)
            if not stack:
                return False
            curr_char = stack.pop()
            if curr_char == '(':
                if char != ")":
                    return False
            if curr_char == '{':
                if char != "}":
                    return False
            if curr_char == '[':
                if char != "]":
                    return False