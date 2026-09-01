balance=100.00
print("This is a bank account based program to help calculate and maintain everyone's balance")
print("The balance starts from 100.00")
print("There are four options 1-Add balance 2-Subtract balance 3-Compound interest")
a=int(input("Please enter the number value of the function you want to perform"))
def add_balance(balance,deposit):
    balance=balance+deposit
    return balance
if(a==1):
    deposit=float(input("Enter the amount to be deposited:"))
    money=add_balance(balance,deposit)
    print("The new balance is {}".format(money))
def subtract_balance(balance,deposit):
    balance=balance-deposit
    return balance
if(a==2):
    deposit=float(input("Enter the amount to be deducted"))
    money=subtract_balance(balance,deposit)
    print("The new balance is {}".format(money))
def compound_interest(balance,rate,time):
    ci=balance*(1+rate/100)**time
    return ci
if(a==3):
    rate=int(input("Please enter the rate for compound interest:"))
    time=int(input("Please enter the time for compound interest:"))
    amount=compound_interest(balance,rate,time)
    print("The amount for compound interest is {}".format(amount))
