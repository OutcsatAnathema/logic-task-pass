class String:
    def __init__(self):
        pass

    def remove_string(self):
        s = input("Enter your sentence: ")
        rs = input("Enter any string you want to remove: ")

        print("\n Your sentence: ", s)

        #replace is a built-in function
        s = s.replace(rs, "")

        print(" Your sentence after removing letter(s): ", s)


s = String()
s.remove_string()
