class String:
    def __init__(self):
        pass

    def occurrence(self):

        s = input("Enter your sentence: ")
        fs = input("Enter a letter: ")

        count = 0
        for i in s:
            if i == fs:
                count += 1

        print(fs, " is occurred ", count, " times.")


s = String()
s.occurrence()
