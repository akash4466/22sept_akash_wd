def account():
    name=input("enter your name:")
    age=int(input("enter your age:"))
    city=input("enter the city name:")
    print("1=hdfc")
    print("2=sbi")
    print("3=axsi")
    print("4=nfty")
    c=int(input("enter the choice:"))

    if c==1:
        bank='hdfc'
    elif c==2:
        bank='sbi'
    elif c==3:
        bank='axis'
    else:
        bank='invalid'
    form={
        'NAME':name,
        'AGE':age,
        'CITY':city,
        'BANK':bank
    }
    print("---account-detail-----")
    for key,value in form.items():
        print(key,':',value)

account()

