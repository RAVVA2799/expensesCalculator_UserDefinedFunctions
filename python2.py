
def calculateExpenses():
 import math
 while True:
    monthlyIncome = input("Enter Monthly Income :")

  
    if  monthlyIncome.isalpha() ==False  and   int(monthlyIncome) >= 100:
       monthlyIncome =int(monthlyIncome)

       rent =input("Add Rent Expenses:")
       food =input("Add Food Expenses :")
       electricity =input("Add Electricity Bill :")
       phone =input("Add Phone Bill:")
       cableTV =input("Add Cable TV Bill:")
       
       expenseCondition = rent.isdigit() and food.isdigit() and electricity.isdigit() and phone.isdigit() and cableTV.isdigit()
       
       
       if expenseCondition == False:
            print("Enter a valid Expenses in Numbers !")
            continue
       elif monthlyIncome >=100  and expenseCondition == True:
           rent =int(rent)
           food  =int(food)
           electricity =int(electricity)
           phone = int(phone)
           cableTV = int(cableTV)

           leftOverAmount =monthlyIncome -(rent+food+electricity+phone+cableTV)

           if leftOverAmount >=0:
               print("LeftOver Amount is $" +str(leftOverAmount))
               break
           else:
              print("Borrowed Amount is $" +str(math.fabs(leftOverAmount)))
              break
       
    else:
        print("Please Add a valid Expenses !")
        
        
calculateExpenses()