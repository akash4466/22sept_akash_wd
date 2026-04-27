class Demo:
    def add(self, a=0, b=0, c=0):
        print(a + b + c)

obj = Demo()
obj.add(2, 3)
obj.add(2, 3, 4)

class A:
    def show(self):
        print("Parent")

class B(A):
    def show(self):
        print("Child")

obj = B()
obj.show()

