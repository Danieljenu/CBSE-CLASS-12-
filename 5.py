import pickle

# Function to create binary file
def create_file():
    f = open("student.dat", "wb")
    n = int(input("Enter number of students: "))

    for i in range(n):
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        mark = int(input("Enter Marks: "))

        student = [roll, name, mark]
        pickle.dump(student, f)

    f.close()
    print("\nBinary file created successfully.\n")


# Function to search for a roll number
def search_file():
    f = open("student.dat", "rb")
    r = int(input("Enter Roll No to search: "))
    found = False

    try:
        while True:
            student = pickle.load(f)
            if student[0] == r:
                print("\nRecord Found")
                print("Name :", student[1])
                print("Marks :", student[2])
                found = True
                break
    except EOFError:
        pass

    if not found:
        print("\nError: Roll No not found")

    f.close()


# Function calls
create_file()
search_file()