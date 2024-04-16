# create account

name = input("Enter Your Name Here: ")
account_no = int(input("Enter Your Account_no Here: "))
balance = int(input("Enter Your Balance Here: "))

# Login
accouno = int(input("Enter Account No: "))
if (account_no == accouno):
    print(f"{name.title()} You've Loged In successfully")
    ch = int(input("Enter choice \n 1.view Details\n2.withdraw\n3.Deposit"))
    match ch:
        case 1:
            print("Account Holder: ", name)
            print("Account_No: ", account_no)
            print("Balance: ", balance)
        case 2:
            withdraw = int(input("Enter Amount to be Withdrawed: "))
            if (balance > withdraw):
                balance -= withdraw
                print("Remaining balance is:", balance)
            else:
                print("Not sufficient amount")
        case 3:
            deposit = int(input("Enter Amount To Be Deposited: "))
            balance += deposit
            print(f"{deposit} Amount Deposited Successfully\n Current Balance is{balance}")

else:
    print(f" Sorry {name.title()},You Entered Wrong Account No! ")