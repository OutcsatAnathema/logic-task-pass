def occurrence():

    s = input("Enter your sentence: ")
    fs = input("Enter a letter: ")

    count = 0
    for i in s:
        if i == fs:
            count += 1

    print(fs, " is occurred ", count, " times.")


occurrence()
