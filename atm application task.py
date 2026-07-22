#atm appliation
while True:
    account=100000
    card=input("enter the card:")
    if card=="c":
        print("welcome srinadh")
        pwd=int(input("enter the pin:"))
        if pwd==1234:
            option=int(input("choose option\n1.balance enquire\n2.amount withdraw:"))
            if option==1:
                print("account balance is:",account)
            elif option==2:
                temp=int(input("enter the amount:"))
                print(temp)
                balance=account-temp
                print("remaining balance is:",balance)
            else:
                print("invalid option")
        else:
            print("incorrect pin")
    else:
        print("invalid card")
