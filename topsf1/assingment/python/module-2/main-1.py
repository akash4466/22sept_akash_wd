n=int(input("enter:"))

the=[]
print("entr the number 1:")
for i in range(n):
    the.append(int(input()))

you=[]
print("enter the number 2:")
for i in range(n):
    you.append(int(input())) 

result=[]
for i in range(n):
    result.append(the[i]+you[i])

print(result)
