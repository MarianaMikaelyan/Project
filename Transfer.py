from Register import User_Database


def account_exists(Account_number):
    for user in User_Database:
        if user["Account_number"] == Account_number:
            return user
    return None

def transfer_balance(sender_account, receiver_account, amount):
    sender = account_exists(sender_account)
    receiver = account_exists(receiver_account)

    if sender is None:
        print("Sender account does not exist.")
        return False
    if receiver is None:
        print("Receiver account does not exist.")
        return False

    sender_balance = sender["Balance"]
    if sender_balance < amount:
        print("Insufficient balance to transfer.")
        return False

    sender["Balance"] -= amount
    receiver["Balance"] += amount
    print(f"You have successfully transferred {amount} from {sender['First_name']} {sender['Last_name']} to {receiver['First_name']} {receiver['Last_name']}")
    return True

def transfer():
    while True:
        sender_account = input("Enter your account number: ")
        sender = account_exists(sender_account)
        if sender:
            break
        else:
            print("Account number not found. Please try again.")

    while True:
        receiver_account = input("Enter the recipient's account number: ")
        receiver = account_exists(receiver_account)
        if receiver:
            break
        else:
            print("Recipient's account number not found. Please try again.")

    while True:
        amount = input("Enter the amount of money to transfer: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Invalid input. Please enter a valid amount.")

    transfer_balance(sender_account, receiver_account, amount)
    print(User_Database)  # This will print the updated database

# Testing the transfer function
if __name__ == "__main__":
    transfer()