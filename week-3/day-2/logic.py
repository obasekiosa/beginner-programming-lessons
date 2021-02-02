
# STACK = []

# def initStack():
#     STACK = []
#     return STACK

def stack():
    return []

def push(stack, item):
    stack.append(item)

def pop(stack):
    return stack.pop()

def size(stack):
    return len(stack)

def isEmpty(stack):
    return size(stack) == 0

def peek(stack):
    item = pop(stack)
    push(stack, item)
    return item


def isBalanced(items):

    s = stack()

    for i in items:
        # get next xter
        if i == "(":
            push(s, i)
        elif i == ")":
            if (isEmpty(s)):
                return False
            else:
                pop(s)

    return True

def main():
    items = "([(])]()())"
    print(isBalanced(items))


main()






