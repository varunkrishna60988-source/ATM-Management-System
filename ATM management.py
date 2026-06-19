balance=1000
pin="20069"
history=[]

enteered_pin=input("enter your ATM pin")
if enteered_pin==pin:
    while True:
        print("\n ===ATM Management system===")
        print("\n 1.check balance")
        print("2.deposite money")
        print("3.withdraw money")
        print("4.change pin")
        print("5.mini statement")
        print("6. exit")

        choice=input("Enter your choice:")
        if choice=="1":
            print("current balance:",balance)

        elif choice=="2":
            amount=int(input("Enter a amount to deposite:"))
            balance+=amount
            history.append(f"deposited{amount}")
            print("Amount deposited successfully")

        elif choice=="3":
            amount=int(input("Enter a amount to withdraw:"))
            if  amount<=balance:
                balance-=amount
                history.append(f"withdrawn{amount}")
            else:
                print("insufficant balance")

        elif choice=="4":
            new_pin=input("Enter a new pin:")
            pin=new_pin
            print("Pin changed successfully")

        elif choice=="5":
            print("\n ===Mini Statement===")
            if len(history)==0:
                print("No transactions")
            else:
                for items in history:
                    print(items)

        elif choice=="6":
            print("Thankyou")
            break
        else:
            print("invalid choice")
else:
        print("wrong pin")



               



      
