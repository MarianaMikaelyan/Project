User_Database = []

def register_user():
    while True:
        First_name = input("Enter your first name: ")
        Last_name = input("Enter your last name: ")
        Account_number = input("Enter your account number: ")
        
        # Check if the account number is valid and unique
        if len(Account_number) == 5 and Account_number[:2] == "TB" and Account_number[2:].isdigit():
            is_unique = True
            for user in User_Database:
                if user["Account_number"] == Account_number:
                    print("Account number already exists. Please enter a unique account number.")
                    is_unique = False
                    break
            if is_unique:
                user_data = {"First_name": First_name, "Last_name": Last_name, "Account_number": Account_number, "Balance": 0}
                User_Database.append(user_data)
                print("You have registered successfully.")
        else:
            print("Invalid Account_number, please enter correct format!")
        
        try:
            A = int(input("If you want to continue registration, enter 1. If not, enter 0: "))
        except ValueError:
            print("Invalid input. Please enter either 0 or 1.")
            continue
        
        if A == 0:
            break
    
    return User_Database

if __name__ == "__main__":
    register_user()