
while True:
    try:
        
        userInput = input("Enter Employee Number :  (123456789A)")
        
        if userInput[:9].isnumeric() and userInput[-1].isalpha() and len(userInput)==10:
            #userInput[-1].upper()
            print(userInput.upper())
            break
        else:
            raise TypeError
    except TypeError:
        print("Error is within:",userInput)
        continue


