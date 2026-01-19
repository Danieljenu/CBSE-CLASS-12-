#Write a Program to create a Binary File to store RollNo, Name and Marks of n students.Search for a RollNo and update the Marks of entered RollNo. If RollNo is not found displayan error message.
import pickle

def create_file():
    f = open("student.dat", "wb")
    n = int(input("Enter number of students: "))

    for i in range(n):
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        record = [roll, name, marks]
        pickle.dump(record, f)

    f.close()
    print("Binary file created successfully")


def update_marks():
    found = False
    new_data = []

    rno = int(input("Enter Roll No to update marks: "))

    f = open("student.dat", "rb")
    try:
        while True:
            record = pickle.load(f)
            if record[0] == rno:
                print("Record Found:", record)
                record[2] = float(input("Enter new marks: "))
                found = True
            new_data.append(record)
    except EOFError:
        pass
    f.close()

    if found:
        f = open("student.dat", "wb")
        for record in new_data:
            pickle.dump(record, f)
        f.close()
        print("Marks updated successfully")
    else:
        print("Error: Roll No not found")


# Function calls
create_file()
update_marks()
