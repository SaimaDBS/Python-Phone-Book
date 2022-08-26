print("###################################")
print("WELCOME TO THE DBS CONSOLE")
print("###################################")

#create an empty list
myList=[]

#input the number of items in the empty list myList
listElements=int(input("Enter the number of elements to be stored in the list : "))
print("\n")

#Prompt the uer to enter the desired number of numbers in the list
print("Input",listElements,"elements in the list \n")

# loop to input the numbers in the list
for i in range(listElements):
    listNumber=int(input(""))
    myList.append(listNumber)
    print("element -",i," : ", myList[i])
    
#Sort the list
myList.sort()

#create a dictionary from the list to get the frequency of the items as value and number as key
counterDictionary={}
i=1
for i in myList:
    counterDictionary[i]=myList.count(i)  
print("\n The frequency of all the items of the list: \n")

# display the value of keys from the dictionary to get the required result of frequency
for key,value in counterDictionary.items():
     print(key,"occurs",value,"times\n")


   