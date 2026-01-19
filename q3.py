def read_and_count():
    f = open("demo.txt", "r")
    text = f.read()
    f.close()

    vowels = 0
    consonants = 0
    lowercase = 0
    uppercase = 0

    for ch in text:
        if ch.isalpha():
            if ch in "aeiouAEIOU":
                vowels += 1
            else:
                consonants += 1

        if ch.islower():
            lowercase += 1
        elif ch.isupper():
            uppercase += 1

    print("Total Vowels:", vowels)
    print("Total Consonants:", consonants)
    print("Total Lowercase characters:", lowercase)
    print("Total Uppercase characters:", uppercase)


# Function call
read_and_count()
