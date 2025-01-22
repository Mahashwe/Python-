# 4. *Simple Payroll System*
#    - *Task:* Create a payroll system where you:
#      - Input an employee's hourly rate and total hours worked.
#      - Calculate gross pay and deduct a flat tax percentage (e.g., 10%).
#      - Display the net pay.
#    - *Concepts Covered:* Input/output, basic arithmetic, and conditional statements.
import time 
def employee():
    name = input("Please Enter your Name:")
    option = int(input(f"Hi,{name} Welcome to payroll.com please choose option 1 To view Salary Slip - 2 To exit:"))
    if option == 1:
        while True:
            role = input(f"{name}, Can you please Enter your Job role:").upper()
            roles = ['IT SUPPORT','AI ENGINEER','DATA ANALYST','UIUX DESIGNER','SALES','HR']
            if role not in roles:
                print(f"Sorry,{name} This role is unreachable")
            else:
                salary(role)
                break
    if option == 2:
        exit()

basic = 1000
basicnew = 2000
def salary(role):
    designation = input("enter your designation for the role:").upper()
    designations = ['INTERN','ASSOCIATE','MANAGER','LEAD']
    if designation not in designations:
        print("Enter a proper designation")
    else:
        hours = int(input("Enter the number of working hours per week:"))
        if designation == 'INTERN' or 'Associate':
            amount = hours * basic
            tax(amount)
        
        
        elif designation == 'LEAD' or 'MANAGER':
            amountnew= hours * basicnew
            tax(amountnew)

def tax(amount):
    print("----------------------SALARY SLIP-----------------")
    print("Here is your total CTC:",amount)
    time.sleep(1)
    pf = 12/100*amount
    print("Your PF is 12 percent of your CTC, your PF:",pf)
    time.sleep(1)
    tax = 10/100 * amount
    print("From the remaining salary 10 percent id deducted as tax: ",tax)
    time.sleep(1)
    base = amount - pf - tax
    time.sleep(1.5)
    print("Your base salary is:",base)









employee()       

    