def calculator() :
    while True :
        try :
            num1 = int(input("enter your first number :  "))
            num2 = int(input("enter your second number  :  "))
            operator = input("enter a operator (+,-,*,/)  :  ")
            if operator not in ["+","-","*","/"] :
                    print("please renter the operator")
                    continue
            return num1,num2,operator
        except ValueError :
             print("invalid input , please try again")

def solve(num1,num2,operator) :
     if operator == "+" :
        return num1 + num2
     elif operator == "-" :
         return num1 - num2
     elif operator == "*" :
         return num1*num2
     else :
         return num1/num2

num1,num2,operator = calculator()
print(solve(num1,num2,operator))
      
