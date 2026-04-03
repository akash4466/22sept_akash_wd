user=set()
n=int(input("enetr the number of elements:"))
for i in range(n):
    value=(input("enter the elements:"))
    user.update(value)
    print("value is",user)