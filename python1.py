

def calculatePay():
    
 while True:
    basicPay =input("Enter Basic Salary :")
    
    if basicPay.isdigit():
        basicPay =int(basicPay)
       
        # 40 % of basic Pay
        directAllowance = (40/100)*basicPay
    
        # 10 % of basic pay
        hra=(10/100)*basicPay

        if basicPay <100:
            print("Enter a Basic Pay greater than $100")
            continue

        else:
            gross_Salary = basicPay + directAllowance + hra
            print("Total Gross Salary is $"+ str(gross_Salary))
        break

    else:
        print("Kindly Enter a Valid Basic Salary")
        
calculatePay()