print("###################################")
print("WELCOME TO THE DBS CONSOLE")
print("###################################")


userName=input("Enter username (DBS\1234): \n")
try:
    name, ext = userName.split('\\')
    if name.isalpha() and ext.isnumeric():
        print("Domain: ",name.upper())
        print("Username: ",ext) 
    elif name.isnumeric() and ext.isalpha():
        print("Domain: ",ext.upper())
        print("Username: ",name) 
    else:
        raise TypeError
        
except TypeError:
    print("Invalid entry")

    



