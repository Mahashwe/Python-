account = 200 #i have set a global variable as account and its balance as 200
def bank():
    global account #while i use global keyword I can update the value of global variable oouside the function and modify teh account varaible as i wish inside the function
    print("====welcome to bank===") 
    while True: #until user clicks exit this will be keep on running
        print("""
            enter 1 to check bank balance
            enter 2 to deposit amount
            enter 3 to withdraw money
            enter 4 to exit the application""")
        
        try:
            num = int(input("enter a number:"))
            if num == 1:
                print("The account balance is :")
                print(account)

            elif num ==2:
                print("enter the amount to be deposited:")
                dep = int(input("enter amount:"))
                total = account + dep 
                print("the current account balance is :")
                print(total)
                account = total 
                # account += dep

            elif num == 3:
                print("Withdraw cash from the bank") 
                withdraw = int(input("enter the amount to be withdrawn:"))
                if withdraw > account : 
                    print("Insufficient bank balance")
                else: 
                    # remains = account - withdraw 
                    # account = remains
                    # print("the remaining balance is",account) 
                    account -= withdraw
                    print("the remaining balance is",account)
            elif num == 4:
                print("exiting the application")  
                exit()  
            else:
                print("CLICK A VALID OPERATION")
        except Exception as e:
            print(f"Invalid operation: {e}")

            
bank()       
