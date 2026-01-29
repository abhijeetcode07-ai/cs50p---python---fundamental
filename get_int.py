def get_int(prompt) :
    while True :
        try :
            num = int(input(prompt))
            return num
        except ValueError :
            print("invalid input, please try again")
result = get_int("Enter your number :  ")
print(result)