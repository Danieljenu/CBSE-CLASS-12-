#Stack Implementation Using List.(PUSH, POP, PEEK and DISPLAY)

stack = []

def push():
    item = int(input("Enter element to push: "))
    stack.append(item)
    print(item, "pushed into stack")


def pop():
    if len(stack) == 0:
        print("Stack is empty. Cannot pop")
    else:
        item = stack.pop()
        print("Popped element:", item)


def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element is:", stack[-1])


def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements:")
        for i in range(len(stack)-1, -1, -1):
            print(stack[i])


while True:
    print("\nSTACK OPERATIONS")
    print("1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("4. DISPLAY")
    print("5. EXIT")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        push()
    elif ch == 2:
        pop()
    elif ch == 3:
        peek()
    elif ch == 4:
        display()
    elif ch == 5:
        print("Exiting program")
        break
    else:
        print("Invalid choice")
