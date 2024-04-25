from Register import User_Database


def account_exists(Account_number):
    for user in User_Database:
        if user["Account_number"] == Account_number:
            return True
    return False
        
def Add_balance(Account_number, new_balance):
    for user in User_Database:
        if user["Account_number"] == Account_number:
            user["Balance"] += new_balance
            return user["Balance"] 

def Addbalance():
    while True:
        Account_number = input("Enter your account number: ")
        if account_exists(Account_number):
            break
        else:
            print("Account number not found. Please try again.")

    while True:
        new_balance = input("Enter the amount of money to be added to the balance: ")
        if new_balance.isdigit():
            new_balance = int(new_balance)
            updated_balance = Add_balance(Account_number, new_balance)
            print("Balance update successful. New balance:", updated_balance)
            break
        else:
            print("Invalid input. Please enter a valid amount.")

    print(User_Database)  # This will print the updated database