import random
import datetime
file=open("era","a")
n=int(input("enter the students :"))
for i in range(n):
    
    x=datetime.datetime.now()
    id=random.randint(1,24)
    name=input("enter the name:")
    city=input("enterbthe city:")
    file.write(f"\ndate:{x}\nid:{id}\nname:{name}\ncity:{city}")


    


