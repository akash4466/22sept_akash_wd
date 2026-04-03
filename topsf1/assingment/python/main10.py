def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

x=int(input("enter the number:"))
y=int(input("enter the number:"))

print("1= addition")
print("2= sub")
print("3= mul")
print("4= divide")

c=int(input("enter the number:"))

if c==1:
    add(x,y)
elif c==2:
    sub(x,y)
elif c==3:
    mul(x,y)
elif c==4:
    div(x,y)
else:
    print("not valid:")









    