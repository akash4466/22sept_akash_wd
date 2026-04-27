class A:
    def show(self):
        print("Class A")

class B(A):
    pass

obj = B()
obj.show()

class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(B):
    pass

obj = C()
obj.show()

class A:
    def show1(self):
        print("A")

class B:
    def show2(self):
        print("B")

class C(A, B):
    pass

obj = C()
obj.show1()
obj.show2()

class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

b = B()
c = C()
b.show()
c.show()

class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

obj = D()
obj.show()

class A:
    def show(self):
        print("Parent")

class B(A):
    def show(self):
        super().show()
        print("Child")

obj = B()
obj.show()
