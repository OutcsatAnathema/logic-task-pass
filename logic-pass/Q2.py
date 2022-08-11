a = int(input("Enter your beginning range: "))
b = int(input("Enter your ending range: "))

for num in range(a, b + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, " is a prime number.")
