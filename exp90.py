def create_stack():
    stack = []
    return stack

#Creating stack an empty stack
def check_empty(stack):
    return len(stack) == 0

#Adding the elements into the stack
def maruthipush(stack, item):
    stack.append(item)
    print("pushed items: " + item)

# Removing an element from the stack
def maruthipop(stack):
    if(check_empty(stack)):
        return "stack is empty"
    return stack.pop()

stack = create_stack()
maruthipush(stack, str(10))
maruthipush(stack, str(20))
maruthipush(stack, str(30))
maruthipush(stack, str(40))
print("popped item: " + maruthipop(stack))
print("popped item: " + maruthipop(stack))
print("popped item: " + maruthipop(stack))
print("popped item: " + maruthipop(stack))
print("popped item: " + maruthipop(stack))