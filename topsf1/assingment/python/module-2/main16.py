print("---akashbank---")
def open():
    global number
    global hname
    global type
    number=int(input("enter your account number:"))
    hname=input("enter your name:")
    type=input("entert type of account:")
    print("---detail---")
    

    dic={
        'A/C NUMBER':number,
        'A/C HOLDER_NAME':hname,
        'TYPE':type
    }
    for key,value in dic.items():
        print(key,':',value)
 
       

def deposite():
    global withdraw
    global amount
    print("---deposit---")
    amount=int(input("enter the amount for deposit:"))
    if amount<2000:
        print("minimum amount should be 2000")
    else:
        print("thank-you for deposit")


def witdraw():
    global x
    print("---ATM---")
    withdraw=int(input("enter amount:"))

    x=withdraw-amount
    print("---AFTER WITHDRAW---")
    
    print(x)


def statment():
    print("holder-number",number),
    print("holder-name",hname)
    print("holder-type",type)

    print("remaning-balance",x)







open()
deposite()
witdraw()
statment()
 