try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")

try:
    f = open("abc.txt", "r")
    x = int(input("Enter number: "))
    print(10 / x)
except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("Division by zero")

try:
    f = open("demo.txt", "r")
    print(f.read())
finally:
    f.close()

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise Exception("Not eligible")
except Exception as e:
    print(e)