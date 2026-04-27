class Student:
    name = "Akash"
    age = 20

obj = Student()
print(obj.name, obj.age)

x = 10

class Demo:
    def show(self):
        x = 5
        print("Local:", x)

obj = Demo()
obj.show()
print("Global:", x)
