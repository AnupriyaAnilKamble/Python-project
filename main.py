from basic import Basic 
from adminmgmt import AdminMgmt 
from customermgmt import CustomerMgmt
from excep import Admin
from excep import Customer


am = AdminMgmt()
cm = CustomerMgmt()
a = Admin()
c = Customer()

User = input(" Are you Admin or Customer?: (a/c) ")
User = User.lower()

if(User == "a"):
        
        successful = False
        for i in range(3):
            Username = input("                                          Enter username: ")
            Password = input("                                          Enter password: ")


    
        
            if (Username == "Admin" and Password == "Admin_1234"):
                print("\n")
                print("                                           !!Login successful!!")
                successful = True
                break

            else:
                print("\n                                             Try again.")
                print("\n")
        
        else:
            print("                                        Try after sometime.")


        if (successful == True) :

            ch = 0
            while(ch != 7):
                print(''' 
                                            1. Add New Car
                                            2. Display exists car list
                                            3. Search 
                                            4. Delete
                                            5. Update by  Model number
                                            6. Purchased car list
                                            7. Exit''')
            
                ch = int(input("Enter your choice: "))
                if (ch==1):
                    MdNo = int(input("Enter Model number: "))
                    x = am.exists(MdNo)
                    if x != 1:
                        MdNm = input("Enter Model Name: ")
                        Ty = input("Enter car type (Petrol/Disel/Petrol+CNG): ")
                        Cr = input("Enter color (Red/Black/White/Silver/Blue/Grey/Ranger Khaki): ")
                        Ec = int(input("Enter engine capacity: "))
                        Pz = int(input("Enter price: "))
                        Qty = int(input("Enter quantity: "))
                    
                        p = Basic(MdNo,MdNm,Ty,Cr,Ec,Pz,Qty)
                        am.addNewModel(p)
                    else:
                        print("Id already exist")
                        break

                    
                elif (ch==2):
                    am.display()

                elif (ch == 3):
                    MdNo = int(input("Enter Model Number: "))
                    am.search(MdNo)

                elif (ch == 4):
                    MdNo = int(input("Enter Model Number: "))
                    am.delete(MdNo)

                elif (ch == 5):
                    MdNo = int(input("Enter Model Number: "))
                    am.update(MdNo)

                elif (ch == 6):
                    am.purchased()

                else:
                    print("----Thank You----")

elif (User == "c"):
    print("                                            !!!Welcome to Hyundai showroom!!!")

    #cm = CustomerMgmt()
    n = 0
    while(n != 4):
        print(''' 
                                    1. Display all models
                                    2. Search by Model Number
                                    3. Purchase
                                    4. Exit''')
            
        n = int(input("Enter your choice: "))
        if (n == 1):
           cm.show()

        elif (n == 2):
            MdNo = int(input("Enter Model Number: "))
            cm.searchbyMdNo(MdNo)

        elif (n == 3):
            MdNo = int(input("Enter Model Number: "))
            cm.purchase(MdNo)
            #c.prettytable()

        else:
            print("Thanks for visiting")

else:
    print("Sorry, incorrect user name!!!!!")