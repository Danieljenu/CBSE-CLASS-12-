#Write a Program to store a string to a file. Read the file and display file content line by line with each word separated by #
#Write a Program to store a string to a file. Read the file and display file content line by line with each word separated by #

def store_string():
    f=open("demo.txt","w")
    while True:
        line=input("enter your line\n")
        f.write(line)
        ch=input("do you want to continue adding more line(y/n)").lower()
        if ch =='y':
            f.write("\n")
            continue
        else:
            break
    print("Text file Added succesfully")
    f.close()

def process_lsit():
    f=open("demo.txt","r")

    for lines in f:
        words = lines.strip().split()   # split line into words
        print("#".join(words))
        
store_string()
process_lsit()
 #or
 #Write a Program to store a string to a file. Read the file and display file content line by line with each word separated by #

# Step 1: Write a string to a file
def write_file2():
    f = open("data.txt", "w")
    text = input("Enter a string to store in file:\n")
    f.write(text)
    f.close()


# Step 2: Read the file and display content
def read_file2():
    f = open("data.txt", "r")
    print("\nFile content with # between words:\n")

    for line in f:
        words = line.split()
        print("#".join(words))

    f.close()


# Function calls
write_file()
read_file()
