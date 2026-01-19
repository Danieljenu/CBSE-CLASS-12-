# Write a Python Program to store roll, name and mark of n students in a csv file and retrieve data from the csv file
import csv

# Function to write data to CSV file
def write_csv():
    n = int(input("Enter number of students: "))

    f = open("students.csv", "w", newline="")
    writer = csv.writer(f)
    writer.writerow(["Roll No", "Name", "Mark"])

    for i in range(n):
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        mark = input("Enter Mark: ")
        writer.writerow([roll, name, mark])

    f.close()
    print("\nData successfully written to CSV file.\n")


# Function to read data from CSV file
def read_csv():
    f = open("students.csv", "r")
    reader = csv.reader(f)

    print("Student Details from CSV file:\n")
    for row in reader:
        print(row)

    f.close()


# Function calls
write_csv()
read_csv()
