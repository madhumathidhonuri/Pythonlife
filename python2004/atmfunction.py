username="madhumathi"
password=6280
user_name=input("enter the username:")
passwords=int(input("enter your 4 digit password:"))
if username==user_name and password==passwords:
   pass
else:
   print("incorrect username or password")
   
s='''
1.credit
2.debit
3.mini statement
4.exit
'''
print(s)
balance=0
amount=0
def credit():
    global balance
    global amount
    credit_amount=int(input("enter the amount to credit:"))
    amount=credit_amount+balance
    print("amount after credit is:",amount)
    balance=amount
    print("total=",balance)

def debit():
    global balance
    global amount
    debit_amount=int(input("enter the amount to debit:"))
    amount=balance-debit_amount
    print("amount after debit is",amount)
    balance=amount
    print("total:",balance)

def checkbalance():
    global balance
    global amount
    balance=amount
    print("total amount is:",balance)

def exit():
    print("exit")

if username==user_name and password==passwords:
    while True:
        option=int(input("enter the option:"))
        if option==1:
          credit()
        elif option==2:
          debit()
        elif option==3:
          checkbalance()
        elif option==4:
          exit()
        else:
          print("incorrect option")
          break
else:
   print("invalid")



