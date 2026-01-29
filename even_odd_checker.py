def check_even_odd():
    while True :
        try :
            x = int(input("Enter the number :  "))
            if x%2 == 0 :
                return "Number is even"
            else :
                return "Number is odd"
        except ValueError :
            print("invalid input please try again")
result = check_even_odd()
print(result)