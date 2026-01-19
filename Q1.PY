def create_list():
    numlist = []
    lim = int(input("Enter your LIMIT: "))
    for i in range(lim):
        num = int(input("Enter your Number: "))
        numlist.append(num)
    print("THE CREATED LIST IS:", numlist)
    return numlist


def change_num(numlist):
    evenum = []
    oddnum = []
    for i in numlist:
        if i % 2 == 0:
            evenum.append(i * 10)
        else:
            oddnum.append(i * 5)

    print("Updated Even Numbers:", evenum)
    print("Updated Odd Numbers:", oddnum)


# Function calls
numbers=create_list()
change_num(numbers)
