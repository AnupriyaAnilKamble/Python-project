import os
from prettytable import PrettyTable

class AdminMgmt:
    def addNewModel(self,p):
        fp = open("data.txt",'a')
        fp.write('\n' + str(p))
        fp.close()

    def display(self):
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
    
    def exists(self,MdNo):
        with open ("data.txt",'r') as fp:
            for p in fp:
                
                try:
                    s = p.split(",")
                    if (s[0] == str(MdNo)):
                        print(p)
                        return 1
                        break

                except ValueError:
                    pass
            else:
                pass

    def search(self,MdNo):
        with open ("data.txt",'r') as fp:
            for p in fp:
                
                try:
                    s = p.split(",")
                    if (s[0] == str(MdNo)):
                        print(p)
                        return 1
                        break

                except ValueError:
                    pass
            else:
                print("Record not found")

    def delete(self,MdNo):
        with open("data.txt",'r') as fp:
            data = []
            found = False
            for p in fp:
                try:
                    p.index(str(MdNo),0,3)

                except ValueError:
                    data.append(p)

                else:
                    found = True

        if (found == True):
            with open("data.txt",'w') as fp:
                for x in data:
                    fp.write(x)

        else:
            print("Record not found")

    def update(self,MdNo):
        found = False
        with open("data.txt",'r') as fp:
            list = []
            for p in fp:
                try:
                    p.index(str(MdNo),0,3)

                except:
                    pass

                else:
                    x = input("Do you want to update model name: (y/n) ")
                    x.lower()

                    if (x == 'y'):
                        name = input("Enter new model name: ")
                        split_data = p.split(',')
                        split_data[1] = name
                        p = ','.join(split_data)

                    x = input("Do you want to update type : (y/n) ")
                    x.lower()

                    if (x == 'y'):
                        type = input("Enter type: ")
                        split_data = p.split(',')
                        split_data[2] = type
                        p = ','.join(split_data)

                    x = input("Do you want to update color : (y/n) ")
                    x.lower()

                    if (x == 'y'):
                        color = input("Enter color : ")
                        split_data = p.split(',')
                        split_data[3] = color
                        p = ','.join(split_data)

                    x = input("Do you want to update price : (y/n) ")
                    x.lower()

                    if (x == 'y'):
                        price = int(input("Enter new price : "))
                        split_data = p.split(',')
                        split_data[5] = str(price)
                        p = ','.join(split_data)

                    x = input("Do you want to update quantity : (y/n) ")
                    x.lower()

                    if (x == 'y'):
                        quantity = int(input("Enter new quantity : "))
                        split_data = p.split(',')
                        split_data[6] = str(quantity) + "\n"
                        p = ','.join(split_data)

                    found = True
                finally:
                    list.append(p)

            if (found == True):
                with open("data.txt", 'w') as fp:
                    for i in list:
                        fp.write(i)
                        #fp.write("\n")

            else:
                print("Data not found")
        
    def purchased(self):
        if(os.path.exists("purchased.txt")):
            with open("purchased.txt",'r') as fp:
                data = []
                for p in fp:
                    s = p.split(",")
                    data.append(s)

                t = PrettyTable()

                t.field_names = ['Model Number','Model Name','Type','Color','Engine Capacity','Price']

                t.title = "Vehicle Details"

                for i in data:
                    t.add_row(i)
                print(t)

    def update1(self,MdNo):
        found = False
        with open("data.txt",'r') as fp:
            list = []
            for p in fp:
                try:
                    p.index(str(MdNo),0,3)

                except:
                    pass

                else:
                    #x = input("Do you want to update quantity : (y/n) ")
                    #x.lower()
                    #if (x == 'y'):
                    quantity = 1
                    
                    split_data = p.split(',')
                    my_qty = split_data[6]
                    #print(type(my_qty), my_qty)
                    var = int(my_qty) - quantity
                    split_data[6] = str(var) + "\n" 
                    #print(split_data[6], type(split_data[6]))
                    p = ','.join(split_data)

                    found = True
                finally:
                    list.append(p)

            if (found == True):
                with open("data.txt", 'w') as fp:
                    for i in list:
                        fp.write(i)
                        #fp.write("\n")

            else:
                print("Data not found")
        