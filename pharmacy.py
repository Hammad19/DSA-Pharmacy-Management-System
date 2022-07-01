import datetime
import os
import random

stack = []

#LinkedList
#BubbleSort
#insertion Sort
#Stack
#Queue
#LinearSearch
#Binary Search
#Array

def bubbleSort(arr):
    n = len(arr)
  
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            arr[j + 1] = key
            
    #3rd Concept
def linearsearch(arr, x):
    for i in range(len(arr)):
        if str(arr[i]) == str(x):
            return i
        else:
            return -1
    

def binary_search(arr, low, high, x):
     
        # Check base case
        if high >= low:
     
            mid = (high + low) // 2
     
            # If element is present at the middle itself
            if int(arr[mid]) == int(x):
                return arr[mid]
     
            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif int(arr[mid]) > int(x):
                return binary_search(arr, low, mid - 1, x)
     
            # Else the element can only be present in right subarray
            else:
                return binary_search(arr, mid + 1, high, x)
     
        else:
            # Element is not present in the array
            return -1
            
class Node:
    def __init__(self, particular, qty, unitprice):
        self.particular = particular
        self.qty = qty
        self.unitprice = unitprice
        self.amount = int(self.qty) * int(self.unitprice)
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.Name = None
        self.company = None
        self.date = None
        self.contact = None
        self.totalbill = 0
        self.start = None
    def insert(self, particular, qty, unitprice):
        if (self.start is None):
            self.start = Node(particular,qty,unitprice)
        else:
            ptr = self.start
            while (ptr.next != None):
                ptr = ptr.next
            ptr.next = Node(particular, qty, unitprice)
    def createinvoice(self):
        self.date = datetime.date.today()
        check = True
        while (check):
            x = str(input('Enter Medicine ID: '))
            qty = str(input('Enter Quantity: '))
            for line in open("medicines.txt", "r").readlines():   
                data=line.split(',')
                if(data[0]== x):
                    particular= data[1]
                    unitprice = data[2]
                      
            self.insert(particular, qty, unitprice)
            self.totalbill += int(qty) * int(unitprice)
            inpt = input("Press Enter to continue to add items or type NO to exit: ")
            if (inpt == "No" or inpt == "no" or inpt == "NO"):
                check = False
    def Print(self):
        self.billno= random.randint(0,5)
        print("\n-------------------------------------------------------------")
        print("Bill:    " + str(self.billno) + "\t\t\t\t\t""Date:    " + str(self.date))
        print("-------------------------------------------------------------")
        print("S/no\tParticular \t\t Qty \t\t Rate  \t\t Amount\n")
        ptr = self.start
        i = 1
        while(ptr != None):
            print(str(i) + "\t\t " + ptr.particular + " \t\t\t " + ptr.qty + " \t\t " + ptr.unitprice + " \t\t " +str(ptr.amount))
            ptr = ptr.next
            i += 1
        print("-------------------------------------------------------------")
        print("\n\t\t\t\t\t\t\t\t\t\t" + "Total: " + str(self.totalbill))
        
class Medicines:
    medicines = []
    def __init__(self,medid,medicinename,price,quantity):
        self.medicineid=medid
        self.medicinename=medicinename
        self.price=price
        self.quantity=quantity
    
    def PurchaseMedicine(self):
        Bill = DoublyLinkedList()
        Bill.createinvoice()
        Bill.Print()
        
    
    def medicinedetails(self):
            file= "medicines.txt"
            if os.path.exists(file):
                for line in open(file, "r").readlines():
                    data = line.split(',')
                    self.medicines.append((data[0]))
        
        
    def FileDeletion(self,file,file2):
         with open(file,"r") as f:
            with open(file2, "w+") as f1:
                for line in f:
                    f1.write(line)
                f.close()
                f1.close()
         if os.path.exists(file):
             os.remove(file)
         else:
            print("The file does not exist")
    
    
    def DisplayAllMedicine(self):
        self.medicines= []
        self.medicinedetails()
        order = int(input("\t1. Ascending Order\n\t2. Descending Order"))
        if(order == 1):
            bubbleSort(self.medicines)
            if(os.path.exists("medicines.txt")):
                for i in range(len(self.medicines)):
                    
                    for line in open("medicines.txt", "r").readlines():   
                        data=line.split(',')
                        if(self.medicines[i] == data[0]):
                            
                            print(str("\n\tMedicine #")+ str(i+1))
                            print("\tID: \t" + str(data[0]))
                            print("\tName: \t" + str(data[1]))
                            print("\tPrice: \t" + str(data[2]))
                            print("\tQuantity: \t" + str(data[3]))    
            else:
                print("\tNo Medicines in Our Pharmacy")
        elif(order == 2):
            bubbleSort(self.medicines)
            if(os.path.exists("medicines.txt")):
                for i in range(len(self.medicines)):
                    #Stack for Descending Sort
                    x = self.medicines.pop()
                    for line in open("medicines.txt", "r").readlines():   
                        data=line.split(',')
                        if(x == data[0]):
                            
                            print(str("\n\tMedicine #")+ str(i+1))
                            print("\tID: \t" + str(data[0]))
                            print("\tName: \t" + str(data[1]))
                            print("\tPrice: \t" + str(data[2]))
                            print("\tQuantity: \t" + str(data[3]))    
            else:
                print("\tNo Medicines in Our Pharmacy")
            
            
        str(input("\tPress Any Key"))    
        
    def DisplayAvailableMedicines(self):
        self.medicines= []
        self.medicinedetails()
        order = int(input("\t1. Ascending Order\n\t2. Descending Order"))
        
        if(order == 2):
            #Sort
            insertion_sort(self.medicines)
            if(os.path.exists("medicines.txt")):
                for i in range(len(self.medicines)):
                    #Queue
                    x = self.medicines.pop(0)
                    for line in open("medicines.txt", "r").readlines():
                        data=line.split(',')
                        if((x == data[0]) and (int(data[3])>0)):
                            print()
                            print(str("\tMedicine #")+ str(i+1))
                            print("\tID: \t" + str(data[0]))
                            print("\tName: \t" + str(data[1]))
                            print("\tPrice: \t" + str(data[2]))
                            print("\tQuantity: \t" + str(data[3]))  
            else:
                print("\tNo Medicines in Our Pharmacy")
            
        elif(order == 1):
            insertion_sort(self.medicines)
            if(os.path.exists("medicines.txt")):
                for i in range(len(self.medicines)):
                    #Stack
                    x = self.medicines.pop()
                    for line in open("medicines.txt", "r").readlines():
                        data=line.split(',')
                        if((x == data[0]) and (int(data[3])>0)):
                            print()
                            print(str("\tMedicine #")+ str(i+1))
                            print("\tID: \t" + str(data[0]))
                            print("\tName: \t" + str(data[1]))
                            print("\tPrice: \t" + str(data[2]))
                            print("\tQuantity: \t" + str(data[3]))  
            else:
                print("\tNo Medicines in Our Pharmacy")
        str(input("\tPress Any Key"))  
        
    
    def DisplayOutofStockMedicines(self):
        if(os.path.exists("medicines.txt")):
            medno=0
            for line in open("medicines.txt", "r").readlines():
                data=line.split(',')
                if(int(data[3])==0):
                    medno+=1
                    print()
                    print(str("\tMedicine #")+ str(medno+1))
                    print("\tID: \t" + str(data[0]))
                    print("\tName: \t" + str(data[1]))
                    print("\tPrice: \t" + str(data[2]))
                    print("\tQuantity: \t" + str(data[3]))  
                  
        else:
            print("\tNo Medicines in Our Pharmacy")
        str(input("\tPress Any Key")) 
        
    def SearchMedicine(self):
        var = True
        for line in open("medicines.txt","r").readlines():
            data = line.split(',')     
            
            #Linear Search
            if(self.medicineid==data[0]):
                
                print("\tID: " + str(data[0]))
                print("\tName: " + str(data[1]))
                print("\tPrice: " + str(data[2]))
                print("\tQuantity: " + str(data[3]))
                str(input("\tPress Any Key To Go Back To The main menu\n\n"))
                
                var = True
            else:
                var = False
        if(var == False):
            print("\tNo Medicine Found")
     
    def ismedalreadytaken(self):
        self.medicines =[]
        self.medicinedetails()
        if(binary_search(self.medicines,0,len(self.medicines)-1,self.medicineid)== -1):
            return False
        else:
            return True
            
    def AddMedicine(self):
        if(self.ismedalreadytaken()==False):
            if(int(self.quantity)>0):
                f = open("medicines.txt","a+")
                f.write(str(self.medicineid) + "," 
                        + str(self.medicinename)+ "," 
                        + str(self.price) +"," 
                        + str(self.quantity) +"," 
                        + "\n")
                print('\n\tMedicine Successfully Added')
                str(input('\n\tPress Any Key'))
            else:
                print("\tPlease enter Quantity greater thn zero")
        else:
            print("\tMedicine ID is Already Taken")
        str(input("\tPress any Key To Continue"))
        
        
    
    def EditMedicine(self):
        file= "medicines.txt"
        file2= "tempmedicines.txt"
        x = open(file2,"w")
        for line in open(file,"r").readlines():
            data = line.split(',')
            print()
            print()
            if(str(self.medicineid)==str(data[0])):
                x.write(str(input('\tEnter New ID: '))+ "," 
                         + str(input('\tEnter New Name: ')) +","
                         + str(input('\tEnter New Price: '))+ ","
                         + str(input('\tEnter Your New Quantity: '))
                         + ",\n")        
            else:
                x.write(str(data[0]) + "," + 
                         str(data[1])+ "," + 
                         str(data[2]) +"," + 
                         str(data[3])+ ",\n" )
                         
        x.close()
        str(input("\n\tSuccessfully Edited\n\tPress Any Key To Go Back To The main menu\n\n"))
        self.FileDeletion(file2,file)
        
    def DeleteMedicine(self):
        file= "medicines.txt"
        file2= "tempmedicines.txt"
        f = open(file,"r")
        f2 = open(file2,"w")
        for line in f.readlines():
            data = line.split(',')
            #Linear Search
            if(str(self.medicineid)==str(data[0])):  
                continue
            else:   
                f2.write(
                    str(data[0]) + "," + 
                    str(data[1])+ "," + 
                    str(data[2]) +"," + 
                    str(data[3]) +",\n" )
                
        f.close()
        f2.close()
        str(input("\n\tSuccessfully Deleted\n\tPress Any Key To Go Back To The main menu\n\n"))
        self.FileDeletion(file2,file)
    
    def DeleteAllMedicines(self):
        confirmation = str(input("Are You Sure You Want To Delete All Contacts Y/N"))
        if (os.path.exists("medicines.txt")) and (confirmation =='Y'):
            os.remove("medicines.txt")
        
class Admin:
    
    users= []
    
    def __init__(self,name,email,password):
        
        self.name=name.lower()
        self.email=email
        self.password = password
        
        
    def getuserids(self):
        
        file= "Admins.txt"
        if os.path.exists(file):
            for line in open(file, "r").readlines():
                data = line.split(',')
                self.users.append(data[1])
        
        
    # def isUserAlreadyRegistered(self):
    #     self.users =[]
    #     self.getuserids()
    #     if(linearsearch(self.users,self.email)==-1):
    #         return False
    #     else:
    #         return True
        
        
    def Register(self):
        if(True):
            f = open("Admins.txt","a+")
            f.write(str(self.name) 
                        + "," + str(self.email)+ "," 
                        + str(self.password)
                        + ",\n")
            print("\tSuccessFully Registered")
        else:
            print("\tEmail already Taken")
        str(input("Press any Key To Move Further"))
        
        
    def Login(self):
        
        x=''
        if(os.path.exists("Admins.txt")):
            for line in open("Admins.txt", "r").readlines():
                data = line.split(',')
                if(self.email==data[1] and self.password == data[2]):
                    self.name = data[0]
                    self.email =data[1]
                    self.password= data[2]
                    self.WelcomeAdmin()
                else:
                    x = 'notfound'
                    
            if(x=='notfound'):
                print("\tInvalid Email or Password")
        else:
            print("\n\tNo User Registered")
            
            
    def WelcomeAdmin(self):
        while(True):
            print('\t\t\t***********************************************')
            print("\t\t\t           "+ self.name+ "! Welcome To Pharmacy ")
            print('\t\t\t***********************************************')
            
            print ("\n\t1. Purchase Medicine   \n\t2. Add Medicine \n\t3. Edit Medicine \n\t4. Search Medicine \n\t5. Delete Medicine \n\t6. Delete All Medicines\n\t7. Display Medicines \n\t8. Display Available Medicines\n\t9. Display Out of Stock Medicines\n\t10. Log Out")
            print()
            select=input("\tEnter Your Selection (1-10): ")
            if select=='1':
                medicines = Medicines('none','none','none','none')
                medicines.PurchaseMedicine()
            
                
            
            elif select=='2':
                
                medicine=Medicines(input("\tEnter Medicine ID:"),
                 input("\tEnter Medicine Name:"),
                 input("\tEnter Medicine Price:"),
                 input("\tEnter Medicine Quantity:"),
                    )
                medicine.AddMedicine()
                
            elif select=='3':
                medicines = Medicines(input("\tEnter Medicine ID:"),'none','none','none')
                medicines.EditMedicine()
                
            elif select=='4':
                medicines = Medicines(input("\tEnter Medicine ID:"),'none','none','none')
                medicines.SearchMedicine()
                
            
            elif select=='5':
                medicines = Medicines(input("\tEnter Medicine ID:"),'none','none','none')
                medicines.DeleteMedicine()
            
            elif select=='6':
                medicines = Medicines('none','none','none','none')
                medicines.DeleteAllMedicines()
            elif select=='7':
                medicines = Medicines('none','none','none','none')
                medicines.DisplayAllMedicine()
                
            elif select=='8':
                medicines = Medicines('none','none','none','none')
                medicines.DisplayAvailableMedicines()
            
            elif select=='9':
                medicines = Medicines('none','none','none','none')
                medicines.DisplayOutofStockMedicines()
                
            elif select=='10':
                break
            
            else:
                print("\tWrong Input")
                
    
            
print('*******************************************************')
print('       P H A R M A C Y          M A N  A G E M E N T ')
print('                     S Y S T E M                     ')
print('*******************************************************')


def start():
    
    while(True):
        print('\t*****************************')
        print("\t           Main Menu")
        print('\t*****************************')
        
       
        print ("\t1. Login  \n\t2. Register \n\t3. Exit")
        print()
        select=input("Enter Your Selection (1-3): ")
        if select=='1':

            admin= Admin('none',input("\tEnter Your Email:"),input("\tEnter Your Password:"),)
            admin.Login()
       
        elif select=='2':
            
            admin= Admin(
                input("\tEnter Your Name:"),input("\tEnter Your Email:"), input("\tEnter Your Password:"))
            admin.Register()
            
        elif select=='3':
            
            break
        
        else:
            print('Wrong Input')
                 

start()