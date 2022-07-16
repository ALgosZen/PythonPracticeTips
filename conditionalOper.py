test = int(input("Enter a number :"))

if test > 0:
    print("positive")
    if (test % 2) == 0:
        print("number is even")
    else:
        print("number is odd")
elif test < 0:
    print("negative")
else:
    print("zero")
