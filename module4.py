
import datetime

employeeFullname=input("Enter Employee Full Name: ") 
while employeeFullname.upper()!="EXIT":
    while True:
        try:
            #employeeFullname=input("Enter Employee Full Name: ") 
            
            if (any(i.isalpha() for i in employeeFullname) and any(i.isspace() for i in employeeFullname) and all(i.isalpha() or i.isspace() for i in employeeFullname)):
                break
            else:
                #print("invalid entry. Try again")
                raise TypeError
        except TypeError:
            print("Invalid Entry. Please enter letters only")
            employeeFullname=input("Enter Employee Full Name: ") 
            #break
    userName=employeeFullname.title()
    print(userName)


    #employeeFullname=employeeFullname.split(" ")

    #employeeNumber=input("Enter Employee Number: ")
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

    #weekEndingdate=input("Enter week Ending Date in format day/month/year: ")
    while True:
        try:
            date = input('Week Ending: (DD/MM/YEAR): ')
            weekEnding = datetime.datetime.strptime(date, "%d/%m/%Y")
            print(date)
            break
        except ValueError:
            print("Sorry, that is in the incorrect format. Try again!")
            continue
    
          

    normalHoursWorked=float(input("Enter number of normal weekly hours allowed to work: "))
    hourRate=float(input("Enter rate per hour: "))
    standardTaxRate=float(input("Enter standard tax rate: "))
    overtimeTaxRate=float(input("Enter overtime tax rate: "))
    overtimeRate=1.5
    normalHoursEarned=normalHoursWorked*hourRate    
    
    
    question=input("Has the emplyee worked overtime Y/N?")
    
    if question.upper()=='Y':
        
        TotaltimeWorked=float(input("Enter number of total number of hours worked including overtime hours: "))
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

    
    
  


