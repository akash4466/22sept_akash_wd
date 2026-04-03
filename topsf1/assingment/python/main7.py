n=int(input("enter the pair you want:"))
akash={}

for i in range(n):
    keys=(input("enter the key:"))
    value=(input("enter the value:"))
    akash[keys]=value

print("final value",akash.items())  

