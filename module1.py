
# https://stackoverflow.com/questions/29460405/checking-if-string-is-only-letters-and-spaces-python


def EmployeeName():
    
    while True:
        try:
            employeeFullname=input("Enter Employee Full Name: ") 
            
            if (any(i.isalpha() for i in employeeFullname) and any(i.isspace() for i in employeeFullname) and all(i.isalpha() or i.isspace() for i in employeeFullname)):
                break
            else:
                print("invalid entry. Try again")
                raise TypeError
        except TypeError:
            print("Please enter letters only")
            continue
    userName=employeeFullname.title()
    print(userName)


    
    #myBook={}

    userName=input("Enter your full name or type Exit to quit: ")

    #employeeFullname=input("Enter Employee Full Name: ") 
    while userName.upper()!="EXIT":
        while True:
            try:
                if (any(i.isalpha() for i in userName) and any(i.isspace() for i in userName) and all(i.isalpha() or i.isspace() for i in userName)):
                    break
                else:
                
                    raise TypeError
            except TypeError:
                print("Invalid Entry. Please enter letters only")
                userName=input("Enter  Full Name: ") 
            
        userName=userName.title()
        print(userName)

    #while userName.upper()!='EXIT':
        userPhone=int(input("Enter phone number: "))
        if userPhone not in myBook.values():
            myBook[userName]=userPhone
            print("Entry Successfull")
        else:
            print("invalid")
            #MenuChoice()
        
        userName=input("Enter your name or type Exit to quit: ")
    print("My Phone Book is: \n",myBook)
    MenuChoice()
        










EmployeeName()
