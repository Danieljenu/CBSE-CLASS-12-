import mysql.connector

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cursor = con.cursor()

# Input EMPID
empid = int(input("Enter Employee ID to search: "))

# SQL query using .format()
query = "SELECT * FROM EMP WHERE EMPID = {}".format(empid)

cursor.execute(query)

record = cursor.fetchone()

# Display result
if record:
    print("Employee Found")
    print("EMPID  :", record[0])
    print("NAME   :", record[1])
    print("DEPT   :", record[2])
    print("SALARY :", record[3])
else:
    print("Employee with given EMPID not found")

# Close connection
con.close()
