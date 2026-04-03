'''stdata={
    'id':[1,2,3,4,5],
    'name':['akash','jay','hat','rishi','pooja'],
    'sub':['math','sci','hindi','computer','gk'],
}
for i,j in stdata.items():
    print(i,j)'''


'''stdata={
    'id':[],
    'name':[],
    'sub':[],
}
n=(input("enter the number of student you want to enter the data:"))
for i in (n):
    id=(input("enter the id:")),
    name=(input("enter the name:")),
    sub=(input("enter the sub:")),

stdata['id'].append(id)
stdata['name'].append(name)
stdata['sub'].append(sub)

for i,j in stdata.items():
    print(i,j)'''

data={}
n=int(input("number of pair:"))
for i in range(n):
    x=input("enter keys:")
    y=input("enetr values:")
    data[x]=y
    
for i in data.items():
    print(i)