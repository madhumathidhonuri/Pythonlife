s='''
1.credit
2.debit
3.mini statement
4.exit
'''

name="madhu"
password="madhu123$$"
user_name=input("enter the name:")
passwords=input("enter the password:")
if name==user_name and password==passwords:
    while True:
      print(s)
      option=int(input("enter the option:"))
      amount=1000
      if  option==1:
          credit_amount=float(input("enter the amount:"))
          print("amount after credit:",credit_amount+amount)
      elif option==2:
            debit_amount=float(input("enter the amount:"))
            print("amount after debit:",debit_amount-amount)
      elif option==3:
            print("amount:",amount)
      elif option==4:
            break
else:
    print("incorrect")
