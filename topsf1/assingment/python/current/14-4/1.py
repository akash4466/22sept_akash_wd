class account_open:
    accounr_number:int
    name:str
    type:str
    
    def getdata(self):
        print("number",self.account_number)
        print("name",self.name)
        print("type",self.type)
        
class deposit:
    amount:int
    def getdeposit(self):
        print("money",self.amount)

        

class withdraw(deposit):
    draw:int
    def getwithdraw(self):
        print("enter the amount",self.amount)
        x=deposit-withdraw
        print("remaining amount:",x)


class statment(deposit,account_open,withdraw):
    statment:str
    def statement(self):
        print("account number:",self.accounr_number)
        print("account holder name:",self.name)
        print("account type:",self.type)

cj=statment()
cj.getdata()
cj.getdeposit()
cj.withdraw()
cj.statement()


    


    
    

    