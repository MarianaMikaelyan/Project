from Register import register_user
from Addbalance import Addbalance
from Transfer import transfer


while True:
    A = int(input("Enter your choice (1: Register, 2: Add Balance, 3. Transfer to another account, 4: Exit): "))
    if A == 1:
        register_user()  
    elif A == 2:
        Addbalance()    
    elif A == 3:
        transfer()    
    elif A == 4:
        break
