#Write a Python Program to read the content of a file. Display the total number of characters, number of words present in file.
def count_file():
    f = open("demo.txt", "r")

    content = f.read()     # read entire file

    char_count = len(content)              # total characters
    word_count = len(content.split())      # total words

    f.close()

    print("Total number of characters:", char_count)
    print("Total number of words:", word_count)


count_file()
