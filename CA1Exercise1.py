
import datetime
#For Employee name and its validation. Name should be with first name and last name with space in between e.g. Saima Saleem
employeeFullname=input("Enter Employee Full Name: ") 
while employeeFullname.upper()!="EXIT":
    while True:
        try:
            if (any(i.isalpha() for i in employeeFullname) and any(i.isspace() for i in employeeFullname) and all(i.isalpha() or i.isspace() for i in employeeFullname)):
                break
            else:
                
                raise TypeError
        except TypeError:
            print("Invalid Entry. Please enter letters only")
            employeeFullname=input("Enter Employee Full Name: ") 
            
    userName=employeeFullname.title()
    print(userName)


    #For the Employee Number and its validation. At the end of 9 digit employee number there is alphabet.
    while True:
        try:
            empNum = input("Enter Employee Number :  (123456789A)")
            if empNum[:9].isnumeric() and empNum[-1].isalpha() and len(empNum)==10:
                empNumber=empNum.upper()
                print(empNumber)
                break
            else:
                raise TypeError
        except TypeError:
            print("Invalid Entry. Try again")
            continue

    # For the date and its validation
    while True:
        try:
            date = input('Week Ending: (DD/MM/YEAR): ')
            weekEnding = datetime.datetime.strptime(date, "%d/%m/%Y")
            print(date)
            break
        except ValueError:
            print("Sorry, this is in the incorrect format. Try again!")
            continue
    
          

    #normalHoursWorked=float(input("Enter number of normal weekly hours allowed to work: "))
    normalHoursWorked=37.5
    hourRate=float(input("Enter rate per hour: "))

    standardTax_Rate=float(input("Enter standard tax rate: (in % eg.20% or 50%)"))
    standardTaxRate=standardTax_Rate/100
    overtimeTax_Rate=float(input("Enter overtime tax rate: (in % eg.20% or 50%)"))
    overtimeTaxRate=overtimeTax_Rate/100
    
    overtimeRate=1.5
    
    normalHoursEarned=normalHoursWorked*hourRate    
    
# For the calculation of overtime if overtime worked    
    question=input("Has the emplyee worked overtime Y/N?")
    
    if question.upper()=='Y':
        
        TotaltimeWorked=float(input("Enter total number of hours worked including overtime hours: "))
        totalOvertimeWorked=TotaltimeWorked-normalHoursWorked
        print("Overtime hours", totalOvertimeWorked)

        totalOvertimeRate=hourRate*overtimeRate
        print("total overtime rate calculated is", totalOvertimeRate)
    
        overtimeEarned=totalOvertimeRate*totalOvertimeWorked
        print("overtimeEarned is:", overtimeEarned)
        
        normalHourTaxDeduction=normalHoursEarned*standardTaxRate 
        overtimeTaxDeduction=overtimeEarned*overtimeTaxRate 
    

    else:
        totalOvertimeWorked=0.0
        overtimeEarned=0.0
        
        normalHoursEarned=normalHoursWorked*hourRate
        
        totalOvertimeRate=hourRate*overtimeRate
        overtimeEarned=totalOvertimeRate*totalOvertimeWorked
                

        normalHourTaxDeduction=normalHoursEarned*standardTaxRate 
        overtimeTaxDeduction=overtimeEarned*overtimeTaxRate 
        
# Payslip Display
    print("\n                             PAYSLIP                     " )
    print(" WEEK ENDING ",date)
    print(" Employee: ",userName) 
    print(" Employee Number:",empNumber )
    print("                 Earnings                  Deductions")
    print("                 Hours   Rate   Total \n")

    
    print("Hours (normal)    {0}  {1}   {2}  Tax  @  20%  {3}".format(normalHoursWorked,hourRate,normalHoursEarned,normalHourTaxDeduction))
    print("Hours (Overtime)  {0}  {1}   {2}  Tax  @  50%  {3}".format(totalOvertimeWorked,totalOvertimeRate,overtimeEarned,overtimeTaxDeduction))                                                      


    x=normalHoursEarned+overtimeEarned
    y=normalHourTaxDeduction+overtimeTaxDeduction

    print("\n                 Total pay:                     ", x)
    print("                 Total deductions:              ", y)

    print("                 Net pay:                       ",x-y )
    
    employeeFullname=input("Enter another Employee Full Name or type Exit: ")    
    
print("End")   

    
    
  


