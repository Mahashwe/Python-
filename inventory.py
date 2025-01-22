#what to do create a inventory tracker to add items, update items and check items - these items have quantity and price attached with it 

def shop():
    
    print("=====WELCOME TO INVENTORY=====")

    inventory = {}
    #n number of items are getting added to same inventory - need to seperate into dicts 

    while True:
        print("===========================================================")
        print("---MANAGE YOUR INVENTORY TRACKER IN ONE APPLICATION---\n")
        print("action 1: Type add to add items to your inventory")
        print("action 2: Type view to view items to your inventory")
        print("action 3: Type update to update items to your inventory")
        print("action 4: Type exit to exit the application")

        ans = int(input("enter operation to be performed:"))
        print(ans)

        if ans == 1:
            print("enter the title of the product")
            title = input("title:")

            if title not in inventory:
                 inventory[title]={}
            
            while True:
                    print(f"Enter the items inside the {title}, enter 'done' if completed")
                    name = input("name of product:")
                    if name == "done":
                        break 
                    quant = input("quantity of item:")
                    inventory[title][name]=quant
            print(inventory)
        
        if ans == 2:
            print("you are viweing the inventory:")
            if inventory is {}:
                 print("the inventory is empty")
            else:
                 print("---------------------------------------------------")
                 print("the stocks present:",inventory)
        
        if ans == 3:
            print("Here is your current inventory:")
            print(inventory)
            while True:
                 print("Press 1 to update to exsisting inventory")
                 print("Press 2 to delt item in exsisting inventory")
                 print("Press 3 to adjust quantity to exsisting inventory")
                 print("Press 4 to delt exsisting inventory")
                 print("Press 5 to exit operation")

                 op = int(input("enter operation to be performed:"))
                 if op == 1:
                      newname =input("add the product name:")
                      newquans=input(f"enter the quantity of {newname}:")
                      inventory[newname]=newquans
                      print("The updated inventory is:",inventory)

                 if op ==2:
                      prod = input("enter the name of product that needs to be delted:")
                      if prod not in inventory:
                           print(f"The item {prod} does not exsist in the inventory")
                      else:
                           del inventory[prod]
                           print("Updated Inventory :",inventory)
                
                 if op ==3:
                      rename=input("enter the name of that product that needs to be renamed in the inventory:")
                      if rename not in inventory:
                           print(f"The value in name of {rename} does not exsist in inventory")
                      else:
                           quans=input("enter the revised quantity:")
                           inventory[rename]=quans
                           print("the updated qunatity :",inventory)
                           
                 if op ==4:
                      print("Now we will be erasing the inventory kindly approve with yes")
                      confirm = input("Enter yes to erase inventory:").lower()
                      if confirm == "yes":
                           username = input("enter username:")
                           while True:
                                password = input("enter password:")
                                if password !="admin123":
                                     print("ACCESS DENIED")
                                else:
                                    inventory.clear()
                                    print("Inventory is deleted:",inventory)
                                    break
                                    
                      else: 
                           print("provide a proper confirmation")

                 if op == 5:
                      print("ALL CHANGES HAVE BEEN RECORDED")
                      exit()
                      

        if ans == 4:
                print("exiting the application")     
                exit()                   

shop()               