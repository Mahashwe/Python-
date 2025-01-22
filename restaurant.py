# Restaurant Billing System*
#    - *Task:* Build a simple billing system for a restaurant:
#      - Display a menu with item prices.
#      - Take orders from a customer (item and quantity).
#      - Calculate and display the total bill.

def restaurant():
    print("----------WELCOME TO HOTEL---------")
    while True:        
        print("Choose 1 to Order")
        print("Choose 2 to exit")
        
        option = int(input("Choose 1 or 2:"))
        if option == 1:
            print("TODAY'S MENU:")
            print("""
                  1.Burger - Price : 150
                  2.Pizza - Price : 270
                  3.Coffee - Price : 30
                  4.Maggie - Price: 60
                  5.Idly - Price : 45
                  
                  """)
            total =[] #declare the list outside of the loop - inorder to append
        while True:
            order = input("Hello - Perform an opertion : Enter dish name to order \n enter done to move to next step \n enter BILL for getting total bill \n Your Operation:").lower()
            if order == "bill":
                choice = int(input("For dine in choose 1\n For delivery choose 2"))
                if choice == 1:
                    print("Your Bill is :",sum(total))
                    break
                if choice == 2:
                    delivery(total)

            menu = {"burger":150,"pizza":270,"coffee":30,"maggie":60,"idly":45}
            if order not in menu:
                print("This Item is currently unavailable")
            elif order in menu:
                price = menu[order]
                print(price)
                total.append(price)
                print(total)
            
            
            if order =="done":
                print("Would you like to have some desserts?")

                op = int(input("choose 1 for desserts or 2 for  FINAL BILL :"))
                if op == 1:
                    print("""
                                    ----Please Choose your dessert--- :
                                    1. Milkshake - Price : 170
                                    2. Ice cream - Price :50
                                    3.Jamun - Price : 85
                                    4.DONE
                                    """)
                    while True:
                        dess = input("Enter name of dessert:").lower()
                        if dess == "done":
                            break

                        dess_menu = {"milkshake":170,"icecream":50,"jamun":85}
                        if dess in dess_menu:
                            price = dess_menu[dess] #dict of the key
                            print(f"{dess} is added to you reciept")
                            print(price)
                            total.append(price)
                            print(total)

                        elif dess not in dess_menu:
                            print("We do not serve this currently")                    
                        
                if op == 2:
                    print(total)
                    print("Your total bill is rupees:",sum(total))
                    break
#########
def delivery(total):
    location = input("Enter your location").lower()
    map = {"anna nagar":20,"central":10,"beach":30,"shenoy nagar":22,"church street":50}
    if location not in map:
        print("We currently dont serve in the specific location")
    if location in map:
        distance = map[location]
        if distance > 30:
            charge = 200
        if distance <= 20:
            charge = 100
        if distance <10:
            charge = 0
        
        print("Your total Bill with delivery charge is",sum(total)+charge)
                
                                   
restaurant()


