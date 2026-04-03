rt=[]
n=int(input("give:"))

for i in range(n):
    id=int(input("enter the id:"))
    name=input("enter the name:")

    no={
        'id':id,
        'name':name
    }
    rt.append(no)

print(rt)