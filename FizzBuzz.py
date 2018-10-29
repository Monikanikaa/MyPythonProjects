numb = int(input("Write your integer: "))

if numb % 3 == 0 and numb % 5 == 0:
    print("FizzBuzz")
elif numb % 3 == 0:
    print("Fizz")
elif numb % 5 == 0:
    print("Buzz")
else:
    print(numb)
input("\nPress Enter to close a file.")