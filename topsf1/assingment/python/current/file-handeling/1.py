file=open("throw","a")
no=int(input("enter the no of students:"))
for i in range (no):
    id=int(input("enter the id:"))
    name=(input("enter the name:"))
    city=(input("enter the city:"))
    file.write(f"\nid:{id}\nname:{name}\ncity:{city}")

    
