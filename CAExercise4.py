


myBook={}

def MenuChoice():
    print("###################################")
    print("MYPY PHONE BOOK")
    print("###################################")

    print("1: Add New Entry")
    print("2: Delete Entry")
    print("3: Update Entry")
    print("4: Lookup Number")
    print("5: Quit")

    menuChoice=int(input("\n Enter the number of your choice from menu \n"))
    if menuChoice==1:
        AddEntry()
    elif menuChoice==2:
        DeleteEntry()
    elif menuChoice==3:
        UpdateEntry()
    elif menuChoice==4:
        LookupEntry()
    elif menuChoice==5:
        ProgramEnd()

# to add the entries to the phone book
def AddEntry():
    
    userName=input("Enter your name or type Exit to quit: ")
    
    # Exception handling for the validation of the correct entry to the userName
    while userName.upper()!='EXIT':
        while True:
            try:
                if (any(i.isalpha() for i in userName) and any(i.isspace() for i in userName) and all(i.isalpha() or i.isspace() for i in userName)):
                
                    break
                else:
                
                    raise TypeError
            except TypeError:
                print("Invalid Entry. Please enter letters only")
                userName=input("Enter  Full Name: ") 

        
        print(userName)

        
    # Exception handling for the validation of the correct entry to the user Phone number. There should not be any alphabets
        while True:
            try:
                userPhone=input("Enter phone number: ")
                if userPhone.isnumeric():
                    if userPhone not in myBook.keys():
                        myBook[userPhone]=userName
                        print("Entry Successfull")
                        break
                        

                    else:
                        print("number already exists. Try another number")
                    
                else:
                    raise TypeError
            except TypeError:
                    print("Invalid Entry. Try again")
                    continue
        
        userName=input("Enter your name or type Exit to quit: ")
    print("My Phone Book is: \n",myBook)
    MenuChoice()
        
#Function to delete the phone number
def DeleteEntry():
    i=0 #check point
    print("My Phone Book is: \n",myBook)
     # Exception handling for the validation of the correct entry to the user Phone number. There should not be any alphabets
    while True:
        try:
            numberDelete = input("Enter the number to delete : ")
            if numberDelete.isnumeric():
                break
            else:
                raise TypeError
        except TypeError:
                    print("Invalid Entry. Try again")
                    continue
# loop used to find number to delete
    for key,val in myBook.items():
        if key==numberDelete:
            print("number found and the corresonding Name is:",val)
            myBook.pop(key)
            print("Number deleted from the Phone Book")
            i+=1
            break
        
    if i==0:
        print("Number Not found")
    print("My Phone Book is: \n",myBook)
    MenuChoice()

# function to update the phone number
def UpdateEntry():
    i=0
    
 # Exception handling for the validation of the correct entry to the user Phone number. There should not be any alphabets
    while True:
        try:
           numberUpdate = input("Enter the number to update : ")
           if numberUpdate.isnumeric():
               break
           else:
               raise TypeError
        except TypeError:
                    print("Invalid Entry. Try again")
                    continue

    
    for key,val in myBook.items():
        
        if key==numberUpdate:
            print("number found and the corresonding Name is:",val)
            nameUpdate=input("Enter the name to update: ")
# Exception handling for the validation of the correct entry to the Name
            while True:
                try:
                    if (any(i.isalpha() for i in nameUpdate) and any(i.isspace() for i in nameUpdate) and all(i.isalpha() or i.isspace() for i in nameUpdate)):
                        myBook[key]=nameUpdate
                        break
                    else:
                        raise TypeError
                except TypeError:
                        print("Invalid Entry. Please enter letters only")
                        nameUpdate=input("Enter  Full Name: ") 
            
            
            print("Updated Phone Book is",myBook)
            i+=1
            break
    if i==0:
        print("Number not found. Please enter more details: ")
        nameToLook=input("Enter Name of the person for which you want to search the number : ")
        NameSearchUpdate(nameToLook)
        
        
                           
    print("My Phone Book is: \n",myBook)
    MenuChoice()
    
# Function to look up the number
def LookupEntry():

    i=0
 # Exception handling for the validation of the correct entry to the user Phone number. There should not be any alphabets    
    while True:
        try:
           numberToLookup=input("Enter number to look up")
           if numberToLookup.isnumeric():
               break
           else:
               raise TypeError
        except TypeError:
                    print("Invalid Entry. Try again")
                    continue
    
    for key,val in myBook.items():
        if numberToLookup in myBook.keys():
            print("number found and the corresonding Name is:",myBook[numberToLookup])
            i+=1
            break
        
    if i==0:
        print("Number not found. Please enter more details: ")
        nameToLook=input("Enter Name of the person for which you want to search the number : ")
        NameSearch(nameToLook)
          
                            
                    
    print("My Phone Book is: \n",myBook)
    MenuChoice()


def NameSearch(name):
    i=0
    while True:
        try:
            if (any(i.isalpha() for i in name) and any(i.isspace() for i in name) and all(i.isalpha() or i.isspace() for i in name)):
                
                break
            else:
                raise TypeError
        except TypeError:
            print("Invalid Entry. Please enter letters only")
            name=input("Enter  Full Name: ") 

    for key,val in myBook.items():
        if name==val:
            print("name found and corresponding number is", key)
            i+=1
            break
    if i==0:
        print("Nothing found")
        

def NameSearchUpdate(name):   
    i=0
    for key,val in myBook.items():
        if name==val:
            print("name found and corresponding number is", key)
            
            updateRecord=input("Do you want to update the phone number? Y/N")
            i+=1
            if updateRecord.upper()=='Y':
                nameUpdate=input("Enter the name to update the record: ")

                while True:
                    try:
                        if (any(i.isalpha() for i in nameUpdate) and any(i.isspace() for i in nameUpdate) and all(i.isalpha() or i.isspace() for i in nameUpdate)):
                            break
                        else:
                            raise TypeError
                    except TypeError:
                        print("Invalid Entry. Please enter letters only")
                        nameUpdate=input("Enter  Full Name: ") 

                myBook[key]=nameUpdate
                print("Updated Phone Book is",myBook)
                
                break
    if i==0:
        print("Nothing found")

def ProgramEnd():

    infoToEnd=input("Do you want to continue the program? Y/N")
    
    if infoToEnd.upper()=='Y':
        MenuChoice()
    else:
        print("Good Bye")
        print("My Phone Book is: \n",myBook)


# to call up the main choice menu
MenuChoice()
    
    
    
    
    

