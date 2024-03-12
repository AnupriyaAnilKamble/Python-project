import os
from excep import Notpresent
from prettytable import PrettyTable
import datetime
from adminmgmt import AdminMgmt

class CustomerMgmt:

    def show(self):
        if(os.path.exists("data.txt")):
            
            with open("data.txt",'r') as fp:
                data = []
                for p in fp:
                    s = p.split(",")
                    data.append(s)

                t = PrettyTable()

                t.field_names = ['Model Number','Model Name','Type','Color','Engine Capacity','Price','Quantity']

                t.title = "Vehicle Details"

                for i in data:
                    t.add_row(i)
                print(t)

    def searchbyMdNo(self,MdNo):
        try:
            with open ("data.txt",'r') as fp:
                for p in fp:
                    s = p.split(",")
                    try:
                        
                        if (s[0] == str(MdNo)):
                            print(p)
                            break

                    except ValueError:
                        pass
                else:
                    raise Notpresent()
        except Notpresent:
            print("Record not found")


   
    def purchase(self,MdNo):
        details =[]
        x = 1
        found = False
        with open("data.txt",'r') as fp:
            for p in fp:       
                s = p.split(",")
                if (str(MdNo) == s[0]):
                    print(p)
                    p.index(str(MdNo),0,3)
                    s = p.split(",")

                    t = int(s[5])
                    #Total_price = t + t*0.28
                    print("Hyundai Showroom")
                    customer_name = input("Enter customer name:")
                    mobile_number = (input("Enter mobile number:"))
                    
                    if mobile_number>=str(7800000000) and mobile_number<=str(9999999999):
                        #if len(mobile_number) == 10:
                        global mobno
                        mobno = str(mobile_number)

                    # mob = []
                    # for i in mobile_number:
                    #     mob.append(i)
                    #print(mob)
                        
                    
                        #print(mobile_number)

                    else:
                        x = 0
                        print("Incorrect mobile number...")
                        break
                    
                    date = datetime.datetime.now()
                    date1 = str(date)
                        

                    t = PrettyTable()
                        
                    t.title = "\n\t\t\t\t\tHyundai Showroom" + "\n\t\t\t\t\t\tBill" + "\nCustomer name:" + customer_name + "\t\t\t\t\t\t\t\tDate Time:" + date1 + "\nMobile no.:" + mobno 
                        
                    t.field_names = ["Model No.","Model Name","Price","Total price = Price + 28% GST"]
                    total = int(s[5]) 
                    t.add_row([s[0],s[1],s[5],total])
                    #t.add_row(["Total bill",Total_price])
                        
                    print(t)
                    found = True
                    with open("purchased.txt",'a') as pur:
                        pur.write('\n'+ str(s[0]) + ',' + str(s[1]) + ',' + str(s[2]) + ',' + str(s[3]) + ',' + str(s[4]) + ',' + str(s[5]))

                    y = int(s[5])
                    print("Please pay", y)
                    x = int(input("Please pay /-Rs amount: "))

                    if (x == y):
                        print("Payment is successful!!! \n Thanks for visiting us....")
                        details.append(p)

                    elif (x < y):
                        print("Insufficient balance.....")

                    else:
                        a = 0
                        a = x - y
                        print("Thanks for visiting us!!!", "Please collect", a, " /-Rs amount.")
                    
                else:
                    details.append(p)
                    #print(details)
                    
                    
                    #z = " ".join(details)
        #print(details)
        if (found == True):
            with open("data.txt","w") as fp:
                for x in details:
                    fp.write(str(x))
                                               
            am = AdminMgmt()
            am.update1(MdNo)                    
                                
        elif(x==1):
            #pass
            print("Record not found.")
                                